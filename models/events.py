from pydantic import BaseModel
from typing import List, Optional

class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

class Config: 
    json_schema_extra = {
        "example": {
            "title": "FastAPI Book Launch",
            "image" : "https://linktomyimage.com/image.png",
            "description": "We will be discussing the contents of the FASTAPI book in this event. Ensure to come with your own copy to wins gifts.",
            "tags": ["fastapi", "book", "launch"],
            "location": "Online"
        }
    }