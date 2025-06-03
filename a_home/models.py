from django.db import models


class Message(models.Model):
    content = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]


class Subscriber(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]
