from app.schemas.event import EventRequest

class EventService:
    async def ingest_event(self, event: EventRequest):
        # For now, we will just return a success message.
        return {
            "status": "accepted",
            "partner_id": event.partner_id,
            "event": event.event_type,
            "message": "Event received and is being processed."
        }