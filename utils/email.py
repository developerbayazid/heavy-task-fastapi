from email.mime.text import MIMEText
from core.config import SMTP_FROM, SMTP_HOST, SMTP_PASSWORD, SMTP_PORT, SMTP_USER
import smtplib

def email_send_util(email_to: str, email_subject: str, email_body: str):
    msg = MIMEText(email_body)
    msg['Subject'] = email_subject
    msg['From'] = SMTP_FROM
    msg['To'] = email_to
    
    try:
        server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.sendmail(SMTP_FROM, email_to, msg.as_string())
        server.quit()
        print("Email sent successfully done!")
    except Exception as e:
        print(e)