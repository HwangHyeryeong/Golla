from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import *
from .messages import *
from .models import Member, Payment, Store
from django.db.models import Sum


@api_view(['POST'])
def createMember(request):
    email = request.data['email']

    if isRegisteredMember(email):
        data = {
            "status": status.HTTP_400_BAD_REQUEST,
            "success": False,
            "message": ALREADY_REGISTERED_MEMBER
        }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
    else:
        serializer = JoinMemberSerializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            data = {
                "status": status.HTTP_200_OK,
                "success": True,
                "message": SUCCESS_JOIN_MEMBER
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            print(f"[ERROR@회원가입]: {serializer.errors}")
            data = {
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "success": False,
                "message": SERVER_ERROR
            }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def login(request):
    email = request.data['email']
    password = request.data['password']

    try:
        member = Member.objects.get(email=email)
        if password == member.password:
            data = {
                "status": status.HTTP_200_OK,
                "success": True,
                "message": SUCCESS_LOGIN,
                "data": {
                    "memberCode": member.memberCode
                }
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = {
                "status": status.HTTP_401_UNAUTHORIZED,
                "success": True,
                "message": FAIL_LOGIN
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)
    except Member.DoesNotExist:
        data = {
            "status": status.HTTP_401_UNAUTHORIZED,
            "success": True,
            "message": FAIL_LOGIN
        }
        return Response(data, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        data = {
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "success": False,
            "message": SERVER_ERROR
        }
        return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def isRegisteredMember(email):
    try:
        member = Member.objects.get(email=email)
        return True
    except Member.DoesNotExist:
        return False
    except Exception as e:
        print(f"[ERROR@가입여부확인]: {e}")
        return False


@api_view(['GET'])
def readMemberInfo(request, memberCode):
    try:
        #회원 기본 정보
        member = Member.objects.get(memberCode=memberCode)
        infoSerializer = MemberSerializer(member).data

        #등급 정보
        grade = Grade.objects.get(gradeCode=member.grade)
        gradeSerializer = GradeSerializer(grade).data

        #구매 합산액
        sumOfPayments = Payment.objects.aggregate(Sum('paymentPrice'))['paymentPrice__sum']

        data = {
            "status": status.HTTP_200_OK,
            "success": True,
            "message": SUCCESS_READ_MEMBER,
            "data":{
                **infoSerializer,
                "totalPayment": sumOfPayments,
                **gradeSerializer,
            }
        }
        return Response(data, status=status.HTTP_200_OK)

    except Member.DoesNotExist:
        data = {
            "status": status.HTTP_404_NOT_FOUND,
            "success": True,
            "message": NOT_FOUND_MEMBER
        }
        return Response(data, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        print(f"[ERROR@회원정보상세조회]: {e}")
        data = {
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "success": False,
            "message": SERVER_ERROR
        }
        return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def readPaymentsHistory(request, memberCode):
    try:
        member = Member.objects.get(memberCode=memberCode) #유효한 사용자인지 검사하는 용도

        payments = Payment.objects.filter(memberCode=memberCode).values()
        paymentsSerializer = PaymentSerializer(payments, many=True).data
        data = {
            "status": status.HTTP_200_OK,
            "success": True,
            "message": SUCCESS_READ_PAYMENTS,
            "data": paymentsSerializer
        }
        return Response(data, status=status.HTTP_200_OK)

    except Member.DoesNotExist:
        data = {
            "status": status.HTTP_404_NOT_FOUND,
            "success": True,
            "message": NOT_FOUND_MEMBER
        }
        return Response(data, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        print(f"[ERROR@회원주문내역조회]: {e}")
        data = {
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "success": False,
            "message": SERVER_ERROR
        }
        return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
