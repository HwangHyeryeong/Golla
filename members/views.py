from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import JoinMemberSerializer
from .messages import *
from .models import Member, Payment


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


def isRegisteredMember(email):
    try:
        member = Member.objects.get(email=email)
        return True
    except Member.DoesNotExist:
        return False
    except Exception as e:
        print(f"[ERROR@가입여부확인]: {e}")
        return False
