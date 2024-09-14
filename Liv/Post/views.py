from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .models import Posts
from .serializer import ListPostSerial, CreatePostSerializer


# Create your views here.
class ListPostView(APIView):

    @swagger_auto_schema(
        operation_description="List posts",
        responses={
            200: openapi.Response(
                description="OK",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,  # The response is an array of post objects
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,    # Each item is an object with the following properties
                        properties={
                            'content': openapi.Schema(type=openapi.TYPE_STRING, description='Post content'),
                            'image': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_BINARY,
                                                    description='image'),
                            'user': openapi.Schema(type=openapi.TYPE_STRING, description='Post creater'),
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

        # Handler for GET request to list all posts
    def get(self, request):
                # Retrieve all posts from the database
        post = Posts.objects.all()
                # Serialize the retrieved posts using ListPostSerial
        serializer = ListPostSerial(post, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreatePost(APIView):
        # Only authenticated users can create posts
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Create a new post",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['content'],
            properties={
                'content': openapi.Schema(type=openapi.TYPE_STRING, description='Content'),
                'image': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_BINARY, description='Picture'),
            }
        ),
        response={ # Possible responses for the 'post' request
            201: openapi.Response(description='Post created successfully'),
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            500: 'Internal Server Error',

        },
    )

        # Handler for POST request to create a new post
    def post(self, request):
                # Initialize the serializer with the request data
        serializer = CreatePostSerializer(data=request.data)
                # Validate the data
        if serializer.is_valid():
                        # Save the post if the data is valid
            serializer.save()
                        # Return the serialized data and a 201 Created status
            return Response(serializer.data, status=status.HTTP_201_CREATED)
                # Return errors if the data is invalid with a 400 Bad Request status
        return Response(serializer.error, status=status.HTTP__400_BAD_REQUEST)
