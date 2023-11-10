from rest_framework import serializers
from .models import Member, Payment, Grade


class JoinMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('name', 'email', 'password', 'nickname', 'grade', 'point', 'joindate')


class MemberSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('memberCode', 'name', 'point')


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('memberCode', 'name', 'email', 'nickname')


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('memberCode', 'name', 'email', 'nickname')


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ('gradeName', 'gradeImg')


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('paymentCode', 'storeCode', 'paymentPrice', 'paymentDate')