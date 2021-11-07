# Twitter API

Building Twitter API using FastAPI framework.

<p align="center">
<img src="https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png">
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
