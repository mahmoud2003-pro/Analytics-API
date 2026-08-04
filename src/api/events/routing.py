from fastapi import APIRouter
from .schemas import Eventschema, EventListSchema, EventCreateSchema, EventUpdateSchema

router = APIRouter()

# Get Data
@router.get("/")
def read_events() -> EventListSchema:
    return {
        "items": [{"id": 1}, {"id": 2}, {"id": 3}]
        }

# Create view
@router.post("/")
def create_event(payload: EventCreateSchema) -> Eventschema:
    print(payload.page)
    return {"id": 123}

@router.get("/{event_id}")
def read_event(event_id: int) -> Eventschema:
    return {"id": event_id}

# Update Data
@router.put("/{event_id}")
def update_event(event_id: int, payload:EventUpdateSchema) -> Eventschema:
    print(payload.description)
    return {"id": event_id}
