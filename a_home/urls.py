from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_view, name="home"),
    path("unsubscribe/<int:id>", views.delete_subscriber, name="unsubscribe"),
]
