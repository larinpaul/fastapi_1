# 2025 06 13

from fastapi import FastAPI

api = FastAPI()


# GET, POST, PUT, DELETE
@api.get('/')
def index():
    return {"message": "Hello World"}


