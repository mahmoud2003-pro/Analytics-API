from fastapi import APIRouter
from .schemas import Eventschema, EventListSchema

router = APIRouter()

@router.get("/")
def read_events() -> EventListSchema:
    return {
        "items": [{"id": 1}, {"id": 2}, {"id": 3}]
        }

@router.get("/{event_id}")
def read_event(event_id: int) -> Eventschema:
    return {"id": event_id}
