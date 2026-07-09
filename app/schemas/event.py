from pydantic import BaseModel

class EventRequest(BaseModel):
    # Define the structure of the incoming event
    partner_id: str
    event_type: str
    payload: dict

class EventResponse(BaseModel):
    # Define the structure of the response after processing the event
    status: str
    partner_id: str
    event_type: str
    message: str