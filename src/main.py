from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from api.events import router as events_router
from api.events.db.session import init_db 
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code to run before the application starts
    init_db()
    yield
    # Code to run after the application shuts down
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)

app.include_router(events_router, prefix="/api/events")

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def read_health():
    return {"status": "ok"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)