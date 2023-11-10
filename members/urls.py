from django.urls import path

from . import views

urlpatterns = [
    path("join", views.createMember, name="createMember"),
    path("login", views.login, name="login"),
    path("info/detail/<memberCode>", views.readMemberInfo, name="readMemberInfo"),
    path("info/simple/<memberCode>", views.readMemberInfoSimple, name="readMemberInfoSimple"),
    path("info/update", views.updateMemberInfo, name="updateMemberInfo"),
    path("payments/<memberCode>", views.readPaymentsHistory, name="readPaymentsHistory"),
]