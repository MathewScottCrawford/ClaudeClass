# 📧 Email AI Pipeline

An AI-powered email processing system using **n8n** + **LangGraph** + **Ollama** — fully local, zero API costs.

Processes Gmail and Yahoo accounts to extract action items, categorize emails, and surface what actually needs your attention.

---

## ✨ Features

- 📥 **Catch-up mode** — works through backlog of old emails in daily batches
- 👀 **Monitor mode** — watches for new emails in near-real-time
- 🤖 **AI classification** — categorizes each email (work, finance, personal, etc.)
- ✅ **Action item extraction** — pulls out tasks, deadlines, and follow-ups
- 🚨 **Urgency scoring** — flags emails that need immediate attention
- 📊 **Google Sheets output** — structured action items you can track
- 📨 **Daily digest** — optional summary email to yourself
- 💰 **100% free** — runs entirely on local LLMs via Ollama

---

## 🏗️ Architecture

```
Gmail / Yahoo
     │
     ▼
  n8n (orchestration + scheduling)
     │
     ▼
  LangGraph Agent (FastAPI)  ←──→  Ollama (local LLMs)
     │
     ▼
  Google Sheets / Email Digest
```

See [`docs/architecture.md`](docs/architecture.md) for full detail.

---

## 🚀 Quick Start

### Prerequisites
- Windows 10/11 with WSL2
- Docker Desktop
- Ollama (https://ollama.com)

### 1. Clone & configure
```powershell
git clone https://github.com/MathewScottCrawford/ClaudeClass.git
cd ClaudeClass
cp .env.example .env
# Edit .env with your values
```

### 2. Pull LLM models
```powershell
ollama pull phi4-mini
ollama pull llama3.1
```

### 3. Start services
```powershell
cd n8n
docker-compose up -d
```

### 4. Open n8n
Navigate to http://localhost:5678

### 5. Import workflows
In n8n UI: **Workflows → Import** → select files from `n8n/workflows/`

---

## 📁 Project Structure

```
ClaudeClass/
├── .env.example              ← copy to .env, fill in values
├── .gitignore
├── README.md
│
├── n8n/
│   ├── docker-compose.yml    ← start everything from here
│   └── workflows/            ← exported n8n workflow JSON files
│
├── agents/
│   ├── email_processor/      ← LangGraph agent (FastAPI service)
│   │   ├── main.py           ← API endpoints
│   │   ├── graph.py          ← LangGraph definition
│   │   ├── nodes.py          ← individual graph nodes
│   │   ├── requirements.txt
│   │   └── Dockerfile
│   └── shared/
│       └── models.py         ← Pydantic schemas
│
└── docs/
    └── architecture.md       ← living architecture document
```

---

## 🔒 Security Notes

- **Never commit `.env`** — it contains encryption keys and passwords
- Credentials for Gmail/Yahoo are stored encrypted inside n8n (not in files)
- The `N8N_ENCRYPTION_KEY` in `.env` protects those stored credentials — back it up

---

## 📚 Development

Built collaboratively with Claude as AI pair programmer.
See `docs/architecture.md` for the decisions log and component details.

### Committing workflow changes
```powershell
# After editing a workflow in n8n UI:
# n8n top-right menu → Download → save to n8n/workflows/
git add n8n/workflows/
git commit -m "feat: <describe what the workflow does now>"
```

---

## 🗺️ Roadmap

- [x] Repo structure and local stack setup
- [ ] Gmail OAuth connection
- [ ] Yahoo IMAP connection
- [ ] Batch catch-up workflow
- [ ] Monitor workflow
- [ ] LangGraph agent (classify + extract)
- [ ] Google Sheets output
- [ ] Daily digest email
- [ ] Urgency notifications
