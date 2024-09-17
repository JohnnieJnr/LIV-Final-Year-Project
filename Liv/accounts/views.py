import random
import string
from .serializer import AccountSerializer, AccountRegistrationSerializer
from .models import Account
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny


def generate_random_username(length=8):
    while True:
        username = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
        if not Account.objects.filter(username=username).exists():
            return username


class RegistrationView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Create a new User",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['last_name', 'first_name', 'email', 'phone', 'password', 'password2'],
            properties={
                'last_name': openapi.Schema(type=openapi.TYPE_STRING),
                'first_name': openapi.Schema(type=openapi.TYPE_STRING),
                'phone': openapi.Schema(type=openapi.TYPE_STRING),
                'email': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING),
                'password2': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
        responses={
            201: 'Created',
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            500: 'Internal Server Error',
        }
    )
    def post(self, request):
        serializer = AccountRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    @swagger_auto_schema(
        operation_description="User logout",
        responses={
            200: openapi.Response(
                description="OK",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'msg': openapi.Schema(type=openapi.TYPE_STRING, description='Response message'),
                    },
                ),
            ),
            401: 'Unauthorized',
            500: 'Internal Server Error',
        }
    )
    def post(self, request):
        logout(request)
        return Response({'msg': 'Successfully Logged out'}, status=status.HTTP_200_OK)


# @method_decorator(csrf_exempt, name='dispatch')
class LoginView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="User login",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='User email'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='User password'),
            },
            required=['email', 'password'],
        ),
        responses={
            200: openapi.Response(
                description="OK",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'msg': openapi.Schema(type=openapi.TYPE_STRING, description='Response message'),
                    },
                ),
            ),
            400: 'Bad Request',
            401: 'Unauthorized',
            500: 'Internal Server Error',
        }
    )
    def post(self, request):
        if 'email' not in request.data or 'password' not in request.data:
            return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)

        email = request.data['email']
        password = request.data['password']

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)

            return Response({'msg': 'Login Success'}, status=status.HTTP_200_OK)

        return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


# @permission_classes([IsAuthenticated, IsAdminUser])
class UserList(APIView):
    @swagger_auto_schema(
        operation_description="List Users",
        responses={
            200: openapi.Response(
                description="OK",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'last_name': openapi.Schema(type=openapi.TYPE_STRING),
                            'first_name': openapi.Schema(type=openapi.TYPE_STRING),
                            'email': openapi.Schema(type=openapi.TYPE_STRING),
                            'phone': openapi.Schema(type=openapi.TYPE_STRING),
                            'date_joined': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
                            'last_login': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
                            'is_active': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                            'is_admin': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                        },
                    ),
                ),
            ),
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            500: 'Internal Server Error',
        }
    )
    def get(self, request):
        user = Account.objects.all()
        serializer = AccountSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
