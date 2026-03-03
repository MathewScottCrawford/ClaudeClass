# ============================================================
#  Email Processor Agent — FastAPI Entry Point
#  Called by n8n via HTTP Request node
# ============================================================
#  Endpoints:
#    POST /process-email   → classify + extract action items
#    GET  /health          → liveness check for n8n
# ============================================================

from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from typing import Optional
import os

# Will be fleshed out in Phase 2
# from graph import build_email_graph

app = FastAPI(
    title="Email Processor Agent",
    description="LangGraph-powered email classification and action extraction",
    version="0.1.0"
)

API_KEY = os.getenv("AGENT_SERVICE_API_KEY", "")


# --- Request / Response Models ------------------------------

class EmailInput(BaseModel):
    message_id: str
    subject: str
    sender: str
    date: str
    body: str
    account: str  # "gmail" or "yahoo"


class ActionItem(BaseModel):
    description: str
    deadline: Optional[str] = None
    priority: str  # "high" | "medium" | "low"


class EmailOutput(BaseModel):
    message_id: str
    category: str          # e.g. "work", "finance", "personal", "newsletter", "spam"
    summary: str
    action_items: list[ActionItem]
    urgency: str           # "urgent" | "normal" | "low"
    requires_response: bool


# --- Routes -------------------------------------------------

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "email-processor-agent"}


@app.post("/process-email", response_model=EmailOutput)
async def process_email(
    email: EmailInput,
    x_api_key: Optional[str] = Header(None)
):
    # Basic API key check (optional but good practice)
    if API_KEY and x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

    # TODO: Wire up LangGraph in Phase 2
    # graph = build_email_graph()
    # result = graph.invoke({"email": email.dict()})

    # Stub response for now — lets us test the n8n → agent connection early
    return EmailOutput(
        message_id=email.message_id,
        category="uncategorized",
        summary=f"[STUB] Subject: {email.subject}",
        action_items=[],
        urgency="normal",
        requires_response=False
    )
