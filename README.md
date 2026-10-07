# 🏠 AI Real Estate Automation Hub

Portfolio project demonstrating AI-powered workflow automation for a real-estate team using **n8n, LLM APIs, Python and Google Workspace/Coda-ready integrations**.

## What it automates

### 1. AI Lead Qualification
A new lead is received → normalized → analyzed by an LLM → classified (buyer / seller / tenant / landlord / other) → scored → summarized → stored → a draft follow-up is generated.

### 2. AI Property Description Generator
Structured property data is converted into a clear, professional property-listing draft. A human validation step is kept before publication.

### 3. Internal Lead Tool
A lightweight Python API exposes lead qualification and listing-generation endpoints, making the automation reusable from n8n or another internal tool.

## Architecture

```text
Form / Email / CRM
       │
       ▼
      n8n
       │
       ├──► LLM API ──► qualification / summary / response
       │
       ├──► Google Sheets / Coda / CRM
       │
       └──► Gmail / team notification

Property data ─► n8n ─► LLM API ─► listing draft ─► human validation ─► website
```

## Stack
- n8n
- LLM API (provider configurable; Claude/OpenAI-compatible adapter can be added)
- Python 3 / FastAPI
- REST APIs / JSON
- Google Workspace or Coda (integration points documented)
- Git / GitHub

## Repository
```text
workflows/   n8n workflow templates
src/         Python internal API + automation logic
data/        safe demo payloads
docs/        architecture and interview demo guide
```

## Quick start

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn src.app:app --reload
```

Open `http://127.0.0.1:8000/docs` to test the API.

### Demo endpoints
- `POST /qualify-lead`
- `POST /generate-listing`
- `GET /health`

The repository works in **demo mode without API credentials**. Set `LLM_API_KEY` and adapt `src/llm.py` to your provider for a live LLM integration.

## n8n
Import the JSON files from `workflows/` into n8n. The included lead workflow is deliberately credential-free and calls the local Python API. Replace the demo/storage nodes with your Google Sheets, Coda, Gmail or CRM credentials in your own n8n instance.

## Engineering choices
- Secrets are never committed; `.env.example` documents configuration.
- LLM output is requested as structured JSON to make downstream automation reliable.
- Human validation is retained for public-facing property content.
- Demo data contains no real personal information.
- Workflow components are separated so providers can be swapped without redesigning the whole automation.

## Why this project
The goal is not only to call an LLM, but to integrate generative AI into a useful business workflow: **capture → understand → decide → store → respond → measure**.

## Author
**Jamal Bahsaine**  
AI / Automation / Software Engineering
