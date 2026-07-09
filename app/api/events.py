from fastapi import APIRouter, Depends

from app.schemas.event import EventRequest, EventResponse
from app.services.event_service import EventService
from app.dependencies import get_event_service

router = APIRouter()

@router.post("/events", response_model=EventResponse)
async def ingest_event(
    event: EventRequest, 
    event_service: EventService = Depends(get_event_service)
    ):
    return await event_service.ingest_event(event)