from pydantic import BaseModel

class EventRequest(BaseModel):
    # Define the structure of the incoming event
    partner_id: str
    event_type: str
    payload: dict