from typing import Dict

from fastapi import FastAPI

from src.controllers import user_controller, tweet_controller


app = FastAPI()

app.include_router(user_controller.router)
app.include_router(tweet_controller.router)


@app.get(path="/")
def root() -> Dict[str, any]:
    return {"message": "Twitter API is running successfully"}
