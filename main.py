from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from agents.buyer_flow_agent import handle_buy_flow_api
from agents.seller_flow_agent import handle_sell_flow_api
from typing import Optional

app = FastAPI(title="AI Real Estate Assistant API")

# Input model for intent detection
class IntentRequest(BaseModel):
    message: str

# Input models for Buy and Sell
class BuyerInfo(BaseModel):
    name: str
    location: str
    phone: str
    email: EmailStr
    budget: Optional[str] = None
    home_type: Optional[str] = None

class SellerInfo(BaseModel):
    name: str
    location: str
    phone: str
    email: EmailStr
    postcode: str

# Endpoint 1: Intent Detection
@app.post("/detect-intent")
def detect_intent(payload: IntentRequest):
    message = payload.message.lower()
    if "buy" in message:
        return {"intent": "BUY"}
    elif "sell" in message:
        return {"intent": "SELL"}
    else:
        raise HTTPException(status_code=400, detail="Intent not recognized. Please include 'buy' or 'sell'.")

# Endpoint 2: Process Buy
@app.post("/process-buy")
def process_buy(buyer: BuyerInfo):
    try:
        # Adjusting argument names to match expected input for handle_buy_flow_api
        result = handle_buy_flow_api(
            name=buyer.name,  # Ensure this matches the parameter name in handle_buy_flow_api
            location=buyer.location,
            phone=buyer.phone,
            email=buyer.email,
            budget=buyer.budget,
            home_type=buyer.home_type,
        )
        return {"message": "Buyer data processed successfully", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint 3: Process Sell
@app.post("/process-sell")
def process_sell(seller: SellerInfo):
    try:
        # Adjusting argument names to match expected input for handle_sell_flow_api
        result = handle_sell_flow_api(
            name=seller.name,  # Ensure this matches the parameter name in handle_sell_flow_api
            location=seller.location,
            phone=seller.phone,
            email=seller.email,
            postcode=seller.postcode,
        )
        return {"message": "Seller data processed successfully", "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
