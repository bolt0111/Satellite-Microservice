# Satellites-Microservice

This add-on exercise implements an additional microservice using Python, Flask/FastAPI, which adds an interactive visual feature to the existing Satellite Tracking App. When a user hovers their mouse over a satellite on the map, the microservice retrieves cities within a 1000 km radius of the satellite with populations over 1,000,000 and displays them on the map.

## Features

- Retrieves cities within a specified radius and minimum population from the microservice API.
- Displays the retrieved cities on the map alongside the satellites.

## Setup Instructions

Follow these steps to set up and run the Satellite Cities Python Microservice:

1. Navigate the folder:

   ```shell
   cd Satellites-Microservice

2. Start the microservice:

   ```shell
   sudo docker build -t satelliteapi .
   sudo docker run -p 5000:5000 --name satelliteapi satelliteapi:1.0

3. The microservice will be available at http://localhost:5000.

Or

1. Install dependences using Python:
   ```shell
   pipenv install
2. Start the microsrevice:
   ```shell
   pipenv run python app.py

## Unit Test
   ```shell
   pytest

