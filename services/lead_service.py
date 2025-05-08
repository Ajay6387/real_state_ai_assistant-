from models.lead_model import Lead
from utils.lead_logger import save_lead as log_lead

def process_lead(lead: Lead):
    log_lead(
        intent=lead.intent,
        name=lead.name,
        location=lead.location,
        phone=lead.phone,
        email=lead.email,
        budget=lead.budget,
        postcode=lead.postcode,
        home_type=lead.home_type
    )