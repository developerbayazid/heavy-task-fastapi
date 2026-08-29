from pydantic import BaseModel, EmailStr

class EmailRequest(BaseModel):
    email_to: EmailStr
    email_subject: str
    email_body: str