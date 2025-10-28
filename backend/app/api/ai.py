from fastapi import APIRouter, Query
from app.services.ai_service import predict_user_name, smart_suggest_issue_description

router = APIRouter()

@router.get("/predict-user")
async def predict_user(partial_name: str):
    directory = ["Alice Smith", "Bob Jones", "Charlie Brown"] # Load from DB in real app
    return await predict_user_name(partial_name, directory)

@router.post("/suggest-description")
async def suggest_description(input_text: str):
    return {"suggestion": await smart_suggest_issue_description(input_text)}