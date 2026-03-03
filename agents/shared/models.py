# ============================================================
#  Shared Models — Used across all agent services
#  Import from here to keep schemas consistent
# ============================================================

from pydantic import BaseModel
from typing import Optional
from enum import Enum


class Category(str, Enum):
    WORK = "work"
    FINANCE = "finance"
    PERSONAL = "personal"
    NEWSLETTER = "newsletter"
    PROMOTIONAL = "promotional"
    SPAM = "spam"
    TRAVEL = "travel"
    RECEIPTS = "receipts"
    SOCIAL = "social"
    UNCATEGORIZED = "uncategorized"


class Priority(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class Urgency(str, Enum):
    URGENT = "urgent"
    NORMAL = "normal"
    LOW = "low"


class ActionItem(BaseModel):
    description: str
    deadline: Optional[str] = None       # ISO date string if detected
    priority: Priority = Priority.MEDIUM
    context: Optional[str] = None        # brief excerpt from email


class ProcessedEmail(BaseModel):
    message_id: str
    account: str
    subject: str
    sender: str
    date: str
    category: Category
    summary: str
    action_items: list[ActionItem]
    urgency: Urgency
    requires_response: bool
    processed_at: Optional[str] = None   # ISO timestamp
