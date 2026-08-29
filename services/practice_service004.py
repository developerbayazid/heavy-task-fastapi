from utils.email import email_send_util
from fastapi import HTTPException
from core.celery_app import celery_app


@celery_app.task(bind=True)
def email_send_service(self, email_to: str, email_subject: str, email_body: str):
    try:
        email_send_util(email_to, email_subject, email_body)
    except Exception as e:
        raise self.retry(exc=e, countdown=10, max_retries=10)