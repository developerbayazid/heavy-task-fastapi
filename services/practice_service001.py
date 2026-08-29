from utils.email import email_send_util
from fastapi import HTTPException

def email_send_service(email_to: str, email_subject: str, email_body: str):
    try:
        email_send_util(email_to, email_subject, email_body)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))