# ============================================================
#  Email Processor Agent — LangGraph Node Functions
#  Each function is one node in the graph.
#  All receive and return EmailState (defined in graph.py)
# ============================================================

# Stub file — implemented in Phase 2 of the tutorial.

from typing import Any

# from langchain_ollama import ChatOllama
# from langchain_core.messages import HumanMessage
# import os


def classify_email(state: dict) -> dict:
    """
    Node 1: Classify the email into a category.
    Categories: work, finance, personal, newsletter,
                promotional, spam, travel, receipts, social
    """
    # TODO: Phase 2
    return {**state, "category": "uncategorized"}


def extract_action_items(state: dict) -> dict:
    """
    Node 2: Extract action items from the email body.
    Looks for: tasks, deadlines, requests, follow-ups,
               decisions needed, approvals required
    """
    # TODO: Phase 2
    return {**state, "action_items": [], "summary": ""}


def assess_urgency(state: dict) -> dict:
    """
    Node 3: Determine urgency level.
    Factors: deadline proximity, sender importance,
             keywords (urgent, ASAP, EOD, etc.), action item count
    """
    # TODO: Phase 2
    return {**state, "urgency": "normal", "requires_response": False}


def format_output(state: dict) -> dict:
    """
    Node 4: Final formatting pass.
    Ensures all fields are present and well-formed
    before returning to FastAPI.
    """
    # TODO: Phase 2
    return state
