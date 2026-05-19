from fastapi import APIRouter

from app.schemas.event import EventRequest
from app.services.event_service import EventService

router = APIRouter()

event_service = EventService()

@router.post("/events")
async def ingest_event(event: EventRequest):
    return await event_service.ingest_event(event)