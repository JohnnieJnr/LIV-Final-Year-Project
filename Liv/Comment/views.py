from django.shortcuts import render
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .models import Comments
from .serializer import ListCommentsSerial, CreateCommentsSerializer


# Create your views here.
class ListCommentView(APIView):

    @swagger_auto_schema(
        operation_description="List Comments",
        responses={
            200: openapi.Response(
                description="OK",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'content': openapi.Schema(type=openapi.TYPE_STRING, description='Post content'),
                            'image': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_BINARY,
                                                    description='image'),
                            'user': openapi.Schema(type=openapi.TYPE_STRING, description='Post creater'),
                            'post': openapi.Schema(type=openapi.TYPE_STRING, description='Post comments'),
                            'created_at': openapi.Schema(type=openapi.TYPE_STRING, description='created_at'),
                        },
                    ),
                ),
            ),
            400: 'Bad Request',
            401: 'Unauthorized request',
            403: 'Forbidden',
            500: 'Internal Server Error',
        }
    )
    def get(self, request):
        coms = Comments.objects.all()
        serializer = ListCommentsSerial(coms, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


# Create your views here.
class CreateComment(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Create a new Comment",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['content'],
            properties={
                'content': openapi.Schema(type=openapi.TYPE_STRING, description='Content'),
                'user': openapi.Schema(type=openapi.TYPE_STRING, description='User'),
                'post': openapi.Schema(type=openapi.TYPE_STRING, description='Post'),
                'image': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_BINARY, description='Picture'),
            }
        ),
        response={
            201: openapi.Response(description='Comments created successfully'),
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            500: 'Internal Server Error',

        },
    )
    def post(self, request):
        serializer = CreateCommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP__400_BAD_REQUEST)
