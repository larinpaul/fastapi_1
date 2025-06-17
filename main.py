# 2025 06 13

from fastapi import FastAPI

api = FastAPI()


# Let's use some pseudo DB, because we will not use SQLAlchemy for now.
# We will use a list of dictionaries to simulate some storage

all_todos = [
    {'todo_id': 1, 'todo_name': 'Sports', 'todo_description': 'Go to the gym'},
    {'todo_id': 2, 'todo_name': 'Read', 'todo_description': 'Read 10 pages'},    
    {'todo_id': 3, 'todo_name': 'Shop', 'todo_description': 'Go shopping'},
    {'todo_id': 4, 'todo_name': 'Study', 'todo_description': 'Study for exam'},
    {'todo_id': 5, 'todo_name': 'Meditate', 'todo_description': 'Meditate 20 minutes'},
]

# We will use something called path parameters...
@api.get('/todos/{todo_id}')
async def get_todo(todo_id: int):
    for todo in all_todos:
        if todo['todo_id'] == todo_id:
            return {'result': todo}

# localhost:9999/ - index endpoint 
# localhost:9999/todos/2
# localhost:9999/todos?first_n=3 # query parameter # that is also part of the url, but it is not a url, it is a query parameter

@api.get('/todos')
def get_todos(first_n: int = None):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos



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
# But it still makes sense to use async def. You can use all of this in FastAPI as well


# We will now imlement and endpoint in an imperfect way... After that we will do it properly just to see the difference.
@api.post('/todos')
def create_todos(todo: dict):
        new_todo_id = max(todo['todo_id'] for todo in all_todos) + 1

        new_todo = {
            'todo_id': new_todo_id,
            'todo_name': todo['todo_name'],
            'todo_description': todo['todo_description']
        }

        all_todos.append(new_todo)

        return new_todo

# We can go to Swagger UI, 127.0.0.1:9999/docs








