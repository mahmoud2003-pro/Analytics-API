from typing import List, Optional
from sqlmodel import SQLModel, Field

class EventModel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    page: Optional[str] = Field(default='')
    description: Optional[str] = Field(default='')

class EventCreateSchema(SQLModel):
    page: str
    description: Optional[str] = Field(default='')

class EventUpdateSchema(SQLModel):
    description: str
    page: Optional[str] = Field(default='')

class EventListSchema(SQLModel):
    items: List[EventModel]
    count: int