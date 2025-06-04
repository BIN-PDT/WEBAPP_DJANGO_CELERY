from datetime import datetime
from celery import shared_task
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .models import Subscriber


@shared_task(name="email_notification")
def send_email_task(subject: str, body: str, emails: list[str]):
    EmailMessage(subject, body, to=emails).send()


@shared_task(name="monthly_newsletter")
def send_newsletter():
    subject = "Monthly Newsletter"
    current_month = datetime.now().strftime("%B")
    emails = [subscriber.email for subscriber in Subscriber.objects.all()]

    body = render_to_string("a_home/newsletter.html", {"month": current_month})
    email = EmailMessage(subject, body, to=emails)
    email.content_subtype = "html"
    email.send()

    subscriber_count = len(emails)
    return f"{current_month} Newsletter to {subscriber_count} subscribers."
