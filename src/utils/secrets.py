from dotenv import load_dotenv
from src.utils.logger import logger

import os


ENV = os.environ.get("ENV")
if ENV == "production":
    dotenv_path = ".env"
    logger.info("Loading production environment variables")
else:
    dotenv_path = ".env.dev"
    logger.info("Loading development environment variables")

exists = os.path.exists(dotenv_path)

if not exists:
    raise Exception("env files don't exist")

load_dotenv(dotenv_path)

ENV = os.environ.get("ENV")
PORT = os.environ.get("PORT")
