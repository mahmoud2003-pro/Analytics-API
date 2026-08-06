from pydantic import BaseModel, Field
from typing import List, Optional

"""
id
page
description
"""

class EventCreateSchema(BaseModel):
    page: str
    description: Optional[str] = Field(default='')

class EventUpdateSchema(BaseModel):
    description: str
    page: Optional[str] = Field(default='')
    
class Eventschema(BaseModel):
    id: int
    page: Optional[str] = Field(default='')
    description: Optional[str] = Field(default='')

class EventListSchema(BaseModel):
    items: List[Eventschema]
