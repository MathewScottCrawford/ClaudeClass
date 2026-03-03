# ============================================================
#  Email Processor Agent — LangGraph Graph Definition
#  This is where the multi-step AI reasoning lives.
#
#  Graph flow:
#    classify_email
#        │
#        ▼
#    extract_action_items
#        │
#        ▼
#    assess_urgency
#        │
#        ▼
#    format_output
# ============================================================

# Stub file — will be fully built in Phase 2 of the tutorial.
# Keeping this here so the repo structure is clear from day one.

from typing import TypedDict, Optional
# from langgraph.graph import StateGraph, END
# from langchain_ollama import ChatOllama
# from nodes import classify_email, extract_action_items, assess_urgency, format_output


# --- State Schema -------------------------------------------

class EmailState(TypedDict):
    # Input
    message_id: str
    subject: str
    sender: str
    date: str
    body: str
    account: str

    # Intermediate results (populated by nodes)
    category: Optional[str]
    summary: Optional[str]
    action_items: Optional[list]
    urgency: Optional[str]
    requires_response: Optional[bool]
    error: Optional[str]


# --- Graph Builder ------------------------------------------

def build_email_graph():
    """
    Builds and compiles the LangGraph email processing graph.
    Returns a compiled graph ready to invoke.

    Usage:
        graph = build_email_graph()
        result = graph.invoke(initial_state)
    """
    # TODO: implement in Phase 2
    # graph = StateGraph(EmailState)
    # graph.add_node("classify", classify_email)
    # graph.add_node("extract_actions", extract_action_items)
    # graph.add_node("assess_urgency", assess_urgency)
    # graph.add_node("format_output", format_output)
    # graph.set_entry_point("classify")
    # graph.add_edge("classify", "extract_actions")
    # graph.add_edge("extract_actions", "assess_urgency")
    # graph.add_edge("assess_urgency", "format_output")
    # graph.add_edge("format_output", END)
    # return graph.compile()
    raise NotImplementedError("Graph not yet implemented — see Phase 2")
