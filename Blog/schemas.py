from pydantic import BaseModel
from typing import List
# A Pydantic model defines what the data coming into API should look like — it’s used for validation and automatic data conversion.
class Blog(BaseModel): #Using Pydantic Model
    title : str
    body : str
    class Config():
        orm_mode = True

# If we wanted to show only title, we could have done the following
# class ShowBlog(BaseModel):
#     title : str
#     class Config():
#         orm_mode = True

class User(BaseModel):
    name : str
    email : str
    password : str


# We use Response Models to control how we want our response to look like

class ShowUser(User): # Response Model for user 
    name : str
    email : str
    blogs : List[Blog] 
    class Config():
        orm_mode = True

class ShowBlog(Blog): # Blog Response Model
    creator : ShowUser
    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None