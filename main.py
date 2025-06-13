# 2025 06 13

from fastapi import FastAPI

api = FastAPI()


# GET, POST, PUT, DELETE
@api.get('/')
def index():
    return {"message": "Hello World"}

# Some endpoints will do something CPU-backed # Doesn't make sense to make it async
@api.get('/calculation')
def calculation():
    # do some heavy calculation
    pass
    return ""

# But what if there is something like getting data from db... It depends on the kind of database request
@api.get('/getdata')
async def get_data_from_db(): 
    await request
    pass
    return "" 

# Some endpoints are going to be synchronous, and some - asynchronous...
# For example, you can receive a request for weather or the stock process in an asynchronous way...

# FastAPI itself, since it runs on scarlett, is still gonna make them async, even if all the endpoints are sync

