from django.urls import path

from . import views

urlpatterns = [
    path("join", views.createMember, name="createMember"),
    path("login", views.login, name="login"),
    path("info/detail/<memberCode>", views.readMemberInfo, name="readMemberInfo"),
    path("payments/<memberCode>", views.readPaymentsHistory, name="readPaymentsHistory"),
]