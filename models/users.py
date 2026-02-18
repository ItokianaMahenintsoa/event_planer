from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.events import Event
from beanie import Document, Link

# class User(BaseModel):
#     email: EmailStr
#     password: str
#     username: str
#     events: Optional[List[Event]] = None

#     class Config:
#         json_schema_extra = {
#                 "example" : {
#                     "email": "fastapi@packt.com",
#                     "password": "strong!!!",
#                     "username": "john_doe",
#                     "events": []
#                 }
#             }
        
class User(Document):
    email: EmailStr
    password: str
    events : Optional[List[Link[Event]]]
    class Settings : 
        name = "users"
    class Config:
        schema_extra = {
            "example" : {
                "email" : "fastapi@packt.com",
                "password" : "strong!!!",
                "events": [],
            }
        }

class TokenResponse(BaseModel):
    access_token: str
    token_type: str


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email" : "fyeventplanner@fastapiapp.com",
                "password" : "strongpassword123"
            }
        }
