from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .models import Events
from .serializer import EventListSerializer, CreateEventsSerializer


# Create your views here.
class ListEventsView(APIView):
    @swagger_auto_schema(
        operation_description="List Events",
        responses={
            200: openapi.Response(
                description="OK",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,  # The response is an array of post objects
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,  # Each item is an object with the following properties
                        properties={
                            'event_name': openapi.Schema(type=openapi.TYPE_STRING, description='Event name'),
                            'description': openapi.Schema(type=openapi.TYPE_STRING, description='Event description'),
                            'event_date': openapi.Schema(type=openapi.TYPE_STRING, description='Event date'),
                            'event_location': openapi.Schema(type=openapi.TYPE_STRING, description='Event date'),
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
    def get(self, request):
        post = Events.objects.all()
        serializer = EventListSerializer(post, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateEvent(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Create   Event",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['event_name', 'event_date'],
            properties={
                'event_name': openapi.Schema(type=openapi.TYPE_STRING, description='event_name'),
                'description': openapi.Schema(type=openapi.TYPE_STRING, description='description'),
                'event_date': openapi.Schema(type=openapi.TYPE_STRING, description='event_date'),
                'event_location': openapi.Schema(type=openapi.TYPE_STRING, description='event_location'),

            }
        ),
        response={
            201: openapi.Response(description='Event created successfully'),
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            500: 'Internal Server Error',

        },
    )
    def post(self, request):
        serializer = CreateEventsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP__400_BAD_REQUEST)

