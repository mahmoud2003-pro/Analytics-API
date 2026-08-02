from pydantic import BaseModel
from typing import List

class Eventschema(BaseModel):
    id: int

class EventListSchema(BaseModel):
    items: List[Eventschema]

