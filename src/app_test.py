import pytest
from flask_testing import TestCase
from app import app, db, City

class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('config.TestingConfig')
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestCitiesResource(BaseTestCase):
    def test_get_cities(self):
        
        city1 = City('Test City 1', 52.5200, 13.4050, 3748148) 
        city2 = City('Test City 2', 48.8566, 2.3522, 2148327) 
        db.session.add(city1)
        db.session.add(city2)
        db.session.commit()

        response = self.client.get('/cities?lat=51.1657&lon=10.4515&radius=1000&min_population=2000000') 

        self.assertEqual(response.status_code, 200)
        json_response = response.get_json()
        print("json_response", json_response)
        self.assertEqual(len(json_response), 13) 


if __name__ == "__main__":
    pytest.main()