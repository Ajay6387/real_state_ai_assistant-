from fastapi import APIRouter, HTTPException
from models.lead_model import Lead
from services.lead_service import process_lead

router = APIRouter()

@router.post("/save-lead/")
def save_lead(lead: Lead):
    try:
        process_lead(lead)
        return {"message": "✅ Lead saved successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"❌ {str(e)}")
