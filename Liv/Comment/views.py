from django.shortcuts import render
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .models import Comments
from .serializer import ListCommentsSerial


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
      # GET method to retrieve the list of comments
    def get(self, request):
                # Query the Comments model to get all comments from the database
        coms = Comments.objects.all()

         # Serialize the comments using the ListCommentsSerial serializer
        # The 'many=True' argument is used because we're serializing multiple comment objects
        # 'context' is passed to include request data for the serializer
        serializer = ListCommentsSerial(coms, many=True, context={'request': request})

                # Return the serialized comment data in the HTTP response with a status of 200 (OK)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Create your views here.
