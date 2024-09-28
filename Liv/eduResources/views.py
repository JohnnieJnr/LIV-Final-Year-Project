from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializer import CreateEduresourcesSerializer, EduReListSerializer
from .models import Eduresources


class CreateEduresource(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Create a new Eduresource",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['title', 'description'],
            properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING, description='Title of the Eduresource'),
                'description': openapi.Schema(type=openapi.TYPE_STRING, description='Description of the Eduresource'),
                'link': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_URI,
                                       description='Resource Link'),
                'resource_type': openapi.Schema(type=openapi.TYPE_STRING,
                                                description='Resource type: Video, Article, Blog'),
            }
        ),
        responses={
            201: openapi.Response(description='Eduresource created successfully'),
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            500: 'Internal Server Error',
        },
    )
    def post(self, request):
        serializer = CreateEduresourcesSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListEduresources(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="List all Eduresources for the authenticated user",
        responses={
            200: openapi.Response(
                description="A list of Eduresources",
                examples={
                    'application/json': [
                        {
                            'id': 1,
                            'title': 'Python Programming Tutorial',
                            'description': 'A comprehensive video tutorial on Python programming.',
                            'link': 'https://example.com/python-tutorial',
                            'resource_type': 'V',
                            'created_at': '2024-09-20T12:34:56Z',
                            'user': 1
                        },
                        {
                            'id': 2,
                            'title': 'Understanding Django',
                            'description': 'An article about the Django framework.',
                            'link': 'https://example.com/django',
                            'resource_type': 'A',
                            'created_at': '2024-09-21T09:23:45Z',
                            'user': 1
                        }
                    ]
                }
            ),
            401: 'Unauthorized',
            500: 'Internal Server Error'
        }
    )
    def get(self, request):
        resources = Eduresources.objects.filter(user=request.user)
        serializer = EduReListSerializer(resources, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)