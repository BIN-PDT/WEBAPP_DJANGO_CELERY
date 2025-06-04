from django.http import HttpRequest
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from .models import Message, Subscriber
from .forms import MessageCreateForm, SubscriberCreateForm
from .tasks import send_email_task


def send_email(message: str):
    subject = "New Message"
    emails = [subscriber.email for subscriber in Subscriber.objects.all()]
    send_email_task.delay(subject, message, emails)


def home_view(request: HttpRequest):
    message_data = Message.objects.all()
    message_form = MessageCreateForm()
    subscriber_data = Subscriber.objects.all()
    subscriber_form = SubscriberCreateForm()

    if request.method == "POST":
        is_message = request.POST.get("content") != None
        if is_message:
            form = MessageCreateForm(request.POST)
            if form.is_valid():
                message = form.save()
                send_email(message.content)
            else:
                messages.error(request, "Opps! Something went wrong.")
        else:
            form = SubscriberCreateForm(request.POST)
            if form.is_valid():
                form.save()
            else:
                messages.error(request, "Opps! Something went wrong.")

        return redirect("home")

    context = {
        "message_data": message_data,
        "message_form": message_form,
        "subscriber_data": subscriber_data,
        "subscriber_form": subscriber_form,
    }
    return render(request, "a_home/home.html", context)


def delete_subscriber(_: HttpRequest, id: int):
    subscriber = get_object_or_404(Subscriber, pk=id)
    subscriber.delete()

    return redirect("home")
