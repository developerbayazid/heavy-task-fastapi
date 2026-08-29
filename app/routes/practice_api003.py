from fastapi import APIRouter, HTTPException, BackgroundTasks
from services.practice_service003 import email_send_util
from schemas.practice_schema003 import EmailRequest



router = APIRouter()

@router.post("/practice003")
async def practice003(data: EmailRequest, background_tasks: BackgroundTasks):
    try:
        background_tasks.add_task(
            email_send_util,
            data.email_to, data.email_subject, data.email_body
        )
        
        return {"message" : "The email has been sent successfully!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))