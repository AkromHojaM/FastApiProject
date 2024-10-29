from fastapi import FastAPI,APIRouter
from pydantic import BaseModel


router = APIRouter()
app = FastAPI()

@app.get('/get_name/')
async def  get_name(name:str):
    try:
        return {'success':True , "message":f"Hello {name}" }
    except Exception as e:
        return {'success':False, 'message':f"Something went wrong {e}" }





# app = FastAPI()
#
# fake_users = [
#     {'id': 1 , 'role': 'admin' , 'name': 'John'},
#     {'id': 2 , 'role': 'user' , 'name': 'Jack'},
#     {'id': 3 , 'role': 'developer' , 'name': 'Jessie'}
# ]
#
#
# class MessageScheme(BaseModel):
#     message:str
#
# class UserScheme(BaseModel):
#     id : int
#     role : str
#     name : str
#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}",response_model=MessageScheme)
# async def hello(name):
#     return {"message":f"Hello {name}"}
#
#
# @app.get("/users")
# async def users_list():
#     return fake_users
#
#
# @app.get("/users/{user_id}")
# async def user_details(user_id: int ):
#     user = list(filter(lambda x:x.get('id') == user_id,fake_users))[0]
#     return user
#
#
# @app.post("/users")
# async def user_create(user: UserScheme):
#
#     fake_users.append(dict(user))
#     return user