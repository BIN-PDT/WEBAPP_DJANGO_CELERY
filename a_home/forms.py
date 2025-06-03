from django import forms
from .models import Message, Subscriber


class MessageCreateForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["content"]
        labels = {"content": ""}
        widgets = {
            "content": forms.TextInput(
                attrs={
                    "placeholder": "Type your message here",
                    "class": "p-4 font-4 text-black outline-none placeholder:italic",
                }
            )
        }


class SubscriberCreateForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ["email"]
        labels = {"email": ""}
        widgets = {
            "email": forms.TextInput(
                attrs={
                    "placeholder": "Register email here",
                    "class": "p-4 font-4 text-black outline-none placeholder:italic",
                }
            )
        }
