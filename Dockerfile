FROM python:3.10

RUN pip3 install pipenv

ENV PROJECT_DIR /usr/src/satellite_microservice

WORKDIR ${PROJECT_DIR}

COPY Pipfile .
COPY Pipfile.lock .
COPY . .

RUN pipenv install --deploy --ignore-pipfile

EXPOSE 5000

CMD ["pipenv", "run", "python", "./src/app.py"]

