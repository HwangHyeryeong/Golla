from rest_framework import serializers
from .models import Member, Payment
from datetime import datetime


class JoinMemberSerializer(serializers.ModelSerializer):
    #기본값 설정
    grade = serializers.IntegerField(default=1)
    point = serializers.IntegerField(default=0)
    joindate = serializers.DateTimeField(default=datetime.now())

    class Meta:
        model = Member
        fields = ('name', 'email', 'password', 'nickname', 'grade', 'point', 'joindate')

