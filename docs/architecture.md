# Email AI Pipeline — Architecture

> Living document. Updated as the system evolves.

---

## Overview

A hybrid n8n + LangGraph system that processes Gmail and Yahoo email accounts:
- **Catch-up mode**: Processes old emails in batches (daily, configurable)
- **Monitor mode**: Watches for new incoming emails in near-real-time
- **AI layer**: Classifies, summarizes, and extracts action items from each email
- **Output**: Structured action items to Google Sheets + optional daily digest email

---

## System Components

```
┌─────────────────────────────────────────────────────────┐
│  n8n (port 5678)          — Orchestration & Scheduling  │
│  LangGraph Agent (port 8000) — AI Processing            │
│  Ollama (port 11434)      — Local LLM Runtime           │
└─────────────────────────────────────────────────────────┘
```

### n8n
- Runs in Docker
- Manages triggers (Schedule, Gmail, IMAP)
- Handles batching, deduplication, routing
- Calls the LangGraph agent via HTTP
- Writes results to output destinations

### LangGraph Agent Service
- FastAPI + LangGraph
- Runs in Docker (or standalone)
- Stateless: each email is an independent invocation
- Uses Ollama for LLM calls (no external API costs)

### Ollama
- Runs natively on Windows (outside Docker) for performance
- Models used:
  - `phi4-mini` — fast classification
  - `llama3.1` — deeper extraction and reasoning

---

## Data Flow

```
Email Account (Gmail / Yahoo)
    │
    ▼
n8n Trigger (Schedule or IMAP Watch)
    │
    ▼
Batch / Filter Node (skip spam, seen emails)
    │
    ▼
HTTP POST → LangGraph Agent (/process-email)
    │
    ▼
LangGraph Graph:
    classify_email → extract_action_items → assess_urgency → format_output
    │
    ▼
Structured JSON response
    │
    ▼
n8n routes result:
    ├── Action items → Google Sheet
    ├── Urgent emails → notification
    └── Daily digest → email to self
```

---

## Workflow Inventory

| File | Description | Status |
|------|-------------|--------|
| `n8n/workflows/email_catchup.json` | Batch processes old emails | 🔲 Planned |
| `n8n/workflows/email_monitor.json` | Watches for new emails | 🔲 Planned |
| `n8n/workflows/daily_digest.json` | Compiles and sends daily summary | 🔲 Planned |

---

## Environment

See `.env.example` for all required environment variables.

Key values:
- `N8N_ENCRYPTION_KEY` — protects stored credentials
- `OLLAMA_BASE_URL` — `http://host.docker.internal:11434` (Docker → Windows Ollama)
- `AGENT_SERVICE_URL` — `http://agent-service:8000` (within Docker network)

---

## Development Workflow

1. Edit workflow in n8n UI
2. Export as JSON: top-right menu → Download
3. Save to `n8n/workflows/`
4. Commit: `git commit -m "feat: <description>"`

For agent changes:
1. Edit Python files in `agents/email_processor/`
2. Rebuild: `docker-compose up -d --build agent-service`
3. Test via n8n or directly: `POST http://localhost:8000/process-email`
4. Commit

---

## Decisions Log

| Date | Decision | Reason |
|------|----------|--------|
| Initial | Ollama runs natively, not in Docker | Better GPU/performance access on Windows |
| Initial | LangGraph agent as separate service | Clean separation; agent can evolve independently |
| Initial | Yahoo via IMAP (not OAuth) | Yahoo OAuth is complex; app passwords are simpler |
