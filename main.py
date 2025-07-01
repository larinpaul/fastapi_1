# 2025 06 13

from enum import IntEnum
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

api = FastAPI()

# Let's define out schemas

class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1

class TodoBase(BaseModel):
    todo_name: str = Field(..., min_length=3, max_length=512, description='Name of the todo')
    todo_description: str = Field(..., description='Description of the todo')
    priority: Priority = Field(default=Priority.LOW, description='Priority of the tood')

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase)
    todo_id: int = Field(..., description='Unique identifier of the todo')

class TodoUpdate(BaseModel): # It is going to inherit from base, but it is going to be optional
    todo_name: Optional[str] = Field(None, min_length=3, max_length=512, description='Name of the todo')
    todo_description: Optional[str] = Field(None, description='Description of the todo')
    priority: Optional[Priority] = Field(None, description='Priority of the tood')    

# Let's use some pseudo DB, because we will not use SQLAlchemy for now.
# We will use a list of dictionaries to simulate some storage

all_todos = [
    Todo(todo_id=1, todo_name='Sports', todo_description='Go to the gym', priority=Priority.MEDIUM),
    Todo(todo_id=2, todo_name='Read', todo_description='Read 10 pages', priority=Priority.LOW),
    Todo(todo_id=3, todo_name='Shop', todo_description='Go shopping', priority=Priority.HIGH),
    Todo(todo_id=4, todo_name='Study', todo_description='Study for exam', priority=Priority.MEDIUM),
    Todo(todo_id=5, todo_name='Meditate', todo_description='Meditate 20 minutes', priority=Priority.LOW),
]

# We will use something called path parameters...
@api.get('/todos/{todo_id}', response_model=Todo)
async def get_todo(todo_id: int):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            return todo

    raise HTTPException(status_code=404, detail='Todo not found')

# localhost:9999/ - index endpoint 
# localhost:9999/todos/2
# localhost:9999/todos?first_n=3 # query parameter # that is also part of the url, but it is not a url, it is a query parameter

@api.get('/todos', response_model=List[Todo])
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
@api.post('/todos', response_model=Todo)
def create_todos(todo: TodoCreate):
        new_todo_id = max(todo.todo_id for todo in all_todos) + 1

        new_todo = Todo(todo_id = new_todo_id,
                        todo_name = todo.todo_name,
                        todo_description = todo.todo_description,
                        priority = todo.priority)

        all_todos.append(new_todo)

        return new_todo

# We can go to Swagger UI, 127.0.0.1:9999/docs
# In Swagger UI, we can write some json for a post, for example like this:
{
    "todo_name": "New Todo",
    "todo_description": "New Todo Description"
}


@api.put('/todos/{todo_id}', response_model=Todo)
def update_todo(todo_id: int, updated_todo: TodoUpdate):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            todo.todo_name = updated_todo.todo_name
            todo.todo_description = updated_todo.todo_description
            todo.priority = updated_todo.priority
            return todo
    raise HTTPException(status_code=404, detail='Todo not found')

@api.delete('/todos/{todo_id}', response_model=Todo)
def delete_todo(todo_id: int):
    for index, todo in enumerate(all_todos)::
        if todo.todo_id == todo_id:
            deleted_todo = all_todos.pop(index)
            return deleted_todo
    raise HTTPException(status_code=404, detail='Todo not found')


# Pydantic schemas and validation # pip3 install pydantic




