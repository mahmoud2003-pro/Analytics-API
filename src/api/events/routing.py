import os
from fastapi import APIRouter
from .models import EventModel, EventListSchema, EventCreateSchema, EventUpdateSchema
from api.events.db.config import DATABASE_URL

router = APIRouter()

# Get Data
@router.get("/")
def read_events() -> EventListSchema:
    print(os.environ.get("DATABASE_URL"), DATABASE_URL)
    return {
        "items": [{"id": 1}, {"id": 2}, {"id": 3}]
        }

# Create view
@router.post("/")
def create_event(payload: EventCreateSchema) -> EventModel:
    print(payload.page)
    data = payload.model_dump() # payload -> dict -> paydantic
    return {"id": 123, **data}

@router.get("/{event_id}")
def read_event(event_id: int) -> EventModel:
    return {"id": event_id}

# Update Data
@router.put("/{event_id}")
def update_event(event_id: int, payload:EventUpdateSchema) -> EventModel:
    print(payload.description)
    data = payload.model_dump()
    return {"id": event_id, **data}
