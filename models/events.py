from pydantic import BaseModel
from typing import List, Optional
from sqlmodel import JSON, SQLModel, Field, Column

class Event(SQLModel, table=True):
    id : int = Field(default=None, primary_key=True)
    title: str
    img: str
    description: str
    tags: List[str] = Field(sa_column=Column(JSON))
    location: str
    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "img" : "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FASTAPI book in this event. Ensure to come with your own copy to wins gifts.",
                "tags": ["fastapi", "book", "launch"],
                "location": "Online"
            }
        }

class EventUpdate(SQLModel):
    title: Optional[str] = None
    img: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    location: Optional[str] = None
    class Config:
        json_schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "img" : "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FASTAPI book in this event. Ensure to come with your own copy to wins gifts.",
                "tags": ["fastapi", "book", "launch", "python"],
                "location": "Google Meet"
            }
        }



# class Event(BaseModel):
#     id: int
#     title: str
#     image: str
#     description: str
#     tags: List[str]
#     location: str

# class Config: 
#     json_schema_extra = {
#         "example": {
#             "title": "FastAPI Book Launch",
#             "image" : "https://linktomyimage.com/image.png",
#             "description": "We will be discussing the contents of the FASTAPI book in this event. Ensure to come with your own copy to wins gifts.",
#             "tags": ["fastapi", "book", "launch"],
#             "location": "Online"
#         }
#     }