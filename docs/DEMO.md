# 3-minute recruiter demo

1. Open the n8n lead workflow and show the Webhook → API → decision flow.
2. Send `data/sample_lead.json` to `/qualify-lead` from FastAPI Swagger.
3. Explain the structured result: intent, priority, score, summary, next action, reply draft.
4. Explain that a production version would store the result in Coda/Google Sheets and send the draft through Gmail after validation.
5. Test `/generate-listing` with `data/sample_property.json` and show the human-validation flag.

## Talking points
- n8n orchestrates the business process; Python contains reusable business/AI logic.
- API boundaries make the system modular and easier to maintain.
- Structured LLM outputs are safer for automation than free-form text.
- Public content is not automatically published: a human validates it first.
- Credentials live in n8n credentials or environment variables, never in Git.
