from fastapi import APIRouter, HTTPException
from schemas.practice_schema002 import EmailRequest
from services.practice_service002 import email_send_service

router = APIRouter()

@router.post("/practice002")
async def practice002(data: EmailRequest):
    try:
        email_send_service(data.email_to, data.email_subject, data.email_body)
        return {"message" : "The email has been successfully done!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))