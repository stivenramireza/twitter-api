from typing import Dict

from fastapi import FastAPI


app = FastAPI()


@app.get(path="/", tags=["Home"])
def home() -> Dict[str, any]:
    return {"message": "Twitter API is running successfully"}
