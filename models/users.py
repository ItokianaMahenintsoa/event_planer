from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.events import Event

class User(BaseModel):
    email: EmailStr
    password: str
    username: str
    events: Optional[List[Event]] = None

    class Config:
        json_schema_extra = {
                "example" : {
                    "email": "fastapi@packt.com",
                    "password": "strong!!!",
                    "username": "john_doe",
                    "events": []
                }
            }
        


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email" : "fyeventplanner@fastapiapp.com",
                "password" : "strongpassword123",
                "events" : []
            }
        }
