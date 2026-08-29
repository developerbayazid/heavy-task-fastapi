from fastapi import APIRouter, HTTPException
from schemas.practice_schema001 import EmailRequest
from services.practice_service001 import email_send_service

router = APIRouter()

@router.post("/practice001")
async def practice001(data: EmailRequest):
    try:
        email_send_service(data.email_to, data.email_subject, data.email_body)
        return {"message" : "The email has been sent successfully!"}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))