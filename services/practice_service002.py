from utils.email import email_send_util
from fastapi import HTTPException
import threading

def email_send_service(email_to: str, email_subject: str, email_body: str):
    try:
        # Heavy process management
        threading.Thread(
            target=email_send_util,
            args=(email_to, email_subject, email_body),
            daemon=True
        ).start()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))