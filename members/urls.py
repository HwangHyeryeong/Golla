from django.urls import path

from . import views

urlpatterns = [
    path("join", views.createMember, name="createMember"),
    path("login", views.login, name="login"),
]