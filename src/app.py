from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Optional
from .automation import qualify_lead, generate_listing

app = FastAPI(title="AI Real Estate Automation Hub", version="1.0.0")

class Lead(BaseModel):
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    message: str
    budget: Optional[float] = None
    city: Optional[str] = None

class Property(BaseModel):
    property_type: str
    city: str
    area_m2: float
    rooms: int
    price: float
    features: list[str] = []

@app.get("/health")
def health():
    return {"status": "ok", "service": "ai-real-estate-automation"}

@app.post("/qualify-lead")
def lead_qualification(lead: Lead):
    return qualify_lead(lead.model_dump())

@app.post("/generate-listing")
def listing_generation(prop: Property):
    return generate_listing(prop.model_dump())
