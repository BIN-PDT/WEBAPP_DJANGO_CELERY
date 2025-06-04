from celery import shared_task
from django.core.mail import EmailMessage


@shared_task
def send_email_task(subject: str, body: str, emails: list[str]):
    EmailMessage(subject, body, to=emails).send()
