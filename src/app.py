from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from geopy.distance import geodesic
import csv
import uuid

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cities.db'
db = SQLAlchemy(app)
cors = CORS(app, resources={r"/*": {"origin": "http://localhost:3000"}})

class City(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    population = db.Column(db.Integer)

    def __init__(self, name, latitude, longitude, population):
        self.id = str(uuid.uuid4())
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.population = population

def load_cities_into_db():
    with app.app_context():
        db.create_all()
        
        with open('./src/assets/cities.csv', 'r') as file:
            cities_reader = csv.DictReader(file)
            for row in cities_reader:
                try:
                    name = row['Name']
                    population = int(row['Population'])
                    coordinates = row['Coordinates'].split(',')
                    latitude = float(coordinates[0])
                    longitude = float(coordinates[1])
                    new_city = City(name, latitude, longitude, population)
                    db.session.add(new_city)
                except ValueError:
                    print(f"Invalid data: {row}")
                    
        db.session.commit()

load_cities_into_db()

class Cities(Resource):
    def get(self):
        lat = request.args.get('lat')
        lon = request.args.get('lon')
        radius = request.args.get('radius')
        min_population = request.args.get('min_population')

        cities = City.query.filter(City.population >= min_population).all()
        result = []
        for city in cities:
            distance = geodesic((lat, lon), (city.latitude, city.longitude))
            if distance <= float(radius):
                result.append({"id": city.id, "name": city.name, "latitude": city.latitude, "longitude": city.longitude, "population": city.population})

        return result

api.add_resource(Cities, '/cities')

if __name__ == '__main__':
    app.run(host="0.0.0.0")
