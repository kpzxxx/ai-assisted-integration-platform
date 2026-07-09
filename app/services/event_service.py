from app.schemas.event import EventRequest, EventResponse

class EventService:
    async def ingest_event(self, event: EventRequest) -> EventResponse:
        # For now, we will just return a success message.
        return EventResponse(
            status="accepted",
            partner_id=event.partner_id,
            event_type=event.event_type,
            message="Event received successfully."
        )