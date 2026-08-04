from pydantic import BaseModel
from typing import List

"""
id
page
description
"""

class EventCreateSchema(BaseModel):
    page: str

class EventUpdateSchema(BaseModel):
    description: str

class Eventschema(BaseModel):
    id: int

class EventListSchema(BaseModel):
    items: List[Eventschema]
