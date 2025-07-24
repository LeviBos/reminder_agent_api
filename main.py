from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class ReminderRequest(BaseModel):
    subject: str
    start: str
    to_address: str

@app.post("/remind")
async def send_reminder(rem_req: ReminderRequest):
    # Hier kun je straks je eigen mail-logica plaatsen
    print(f"Reminder versturen: {rem_req.subject}, {rem_req.start}, {rem_req.to_address}")
    # Dummy response
    return {"status": "reminder sent", "subject": rem_req.subject, "to": rem_req.to_address}
