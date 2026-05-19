from fastapi import APIRouter

from app.schemas.event import EventRequest

router = APIRouter()

@router.post("/events")
async def ingest_event(event: EventRequest):
    # Process the incoming event
    return {"status": "accepted",
     "partner_id": event.partner_id,
     "event": event.event_type,
     "message": "Event received and is being processed."}