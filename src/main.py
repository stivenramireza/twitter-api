from fastapi import FastAPI

from src.utils.logger import logger

import uvicorn


app = FastAPI()


def main() -> None:
    logger.info(f"Twitter API is running at port {PORT} in {ENV} mode")
    uvicorn.run(app, host="0.0.0.0", port=PORT)


if __name__ == "__main__":
    main()
