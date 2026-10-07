from .llm import llm_json

def qualify_lead(lead: dict) -> dict:
    prompt = f'''You are an assistant for a real-estate team.
Analyze this lead and return JSON with: intent, priority (low/medium/high), score (0-100), summary, next_action, reply_draft.
Lead: {lead}'''
    fallback = {
        "intent": "buyer" if "achet" in lead["message"].lower() else "other",
        "priority": "medium",
        "score": 65,
        "summary": f"Lead from {lead['name']} interested in real estate in {lead.get('city') or 'unspecified area'}.",
        "next_action": "Review the request and contact the lead.",
        "reply_draft": f"Bonjour {lead['name']}, merci pour votre message. Nous revenons vers vous rapidement afin d'échanger sur votre projet."
    }
    result = llm_json(prompt, fallback)
    return {"lead": lead, "qualification": result, "human_review_required": True}

def generate_listing(prop: dict) -> dict:
    prompt = f'''Write a concise professional French real-estate listing from this structured property data. Return JSON with title, description, highlights. Do not invent facts. Property: {prop}'''
    features = ", ".join(prop.get("features", [])) or "caractéristiques à préciser"
    fallback = {
        "title": f"{prop['property_type']} {prop['rooms']} pièces – {prop['city']}",
        "description": f"Découvrez ce {prop['property_type'].lower()} de {prop['area_m2']} m² situé à {prop['city']}, proposé à {prop['price']:.0f} €. Il comprend {prop['rooms']} pièces. Points à retenir : {features}.",
        "highlights": prop.get("features", [])
    }
    return {"property": prop, "draft": llm_json(prompt, fallback), "publication_status": "human_validation_required"}
