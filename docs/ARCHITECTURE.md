# Architecture

## Lead workflow
Webhook/Form → n8n → Python REST API → LLM qualification → IF priority → storage → response draft / notification.

## Listing workflow
Property payload → n8n/Python API → LLM content generation → human validation → website/CMS.

## Production extensions
- Google Sheets: append/update lead rows.
- Coda: upsert leads into a table via API.
- Gmail: create a draft or send after approval.
- Website/CMS: publish only after explicit validation.
- Observability: execution status, errors, latency and token/cost tracking.
