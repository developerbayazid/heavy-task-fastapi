from fastapi import APIRouter, HTTPException
from schemas.practice_schema004 import EmailRequest
from services.practice_service004 import email_send_service

router = APIRouter()

@router.post("/practice004")
async def practice004(data: EmailRequest):
    try:
        task = email_send_service.delay(data.email_to, data.email_subject, data.email_body)
        return {
            "message" : "The email has been sent successfully!",
            "task_id" : task.id
        }
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))