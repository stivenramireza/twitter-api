from typing import Dict

from fastapi import FastAPI

from src.controllers import user_controller, tweet_controller


app = FastAPI(title="Twitter API")


@app.get(path="/", tags=["Home"])
def root() -> Dict[str, any]:
    return {"message": "Twitter API is running successfully"}


app.include_router(user_controller.router)
app.include_router(tweet_controller.router)
