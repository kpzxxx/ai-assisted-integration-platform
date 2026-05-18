from fastapi import FastAPI

app = FastAPI(
    title="AI-Assisted Integration platform",
    version="0.1.0"
)

@app.get("/health")
async def health(): 
    return {"status": "ok"}

# endpoint for partner event ingestion
@app.post("/events")
async def ingest_event(event: dict):
    # Process the incoming event
    return {"status": "success", "event": event}