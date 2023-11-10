from rest_framework import serializers
from .models import Member, Payment, Grade
from django.utils import timezone


class JoinMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('name', 'email', 'password', 'nickname', 'grade', 'point', 'joindate')


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('memberCode', 'name', 'point')


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ('gradeName', 'gradeImg')


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('paymentcode', 'storecode', 'paymentPrice', 'paymentdate')