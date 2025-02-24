import requests
from application.ports import EmailService

class ExternalEmailService(EmailService):
    def send_email(self, recipient: str, subject: str, body: str) -> bool:
        response = requests.post("https://api.emailservice.com/send", json={"to": recipient, "subject": subject, "body": body})
        return response.status_code == 200