# Twitter API

Building Twitter API using FastAPI framework.

<p align="center">
<img src="https://user-images.githubusercontent.com/31974084/140669155-cc9f1e0a-d76e-4479-9c3d-1b883821782b.png">
</p>

## Run API in development mode

    $ python3 -m venv twitter-api
    $ source twitter-api/bin/activate
    $ pip install -r requirements.txt
    $ export ENV=development
    $ uvicorn src.main:app --reload

## Run API in production mode

    $ docker build -t stivenramireza/twitter-api:latest .
	$ docker-compose up -d
