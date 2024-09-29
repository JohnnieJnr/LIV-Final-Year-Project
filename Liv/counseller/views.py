from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Counsellor
from .serializer import CreateCounsellorSerializer, CounsellorSerializer


class ListCounsellorView(APIView):

    @swagger_auto_schema(
        operation_description="List all Counsellors",
        responses={
            200: openapi.Response(
                description="OK",
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'name': openapi.Schema(type=openapi.TYPE_STRING, description='Counsellor Name'),
                            'languages_spoken': openapi.Schema(type=openapi.TYPE_STRING,
                                                               description='Languages Spoken'),
                            'phone': openapi.Schema(type=openapi.TYPE_STRING, description='Phone Number'),
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
        counsellors = Counsellor.objects.all()  # Fetch all counsellor records
        serializer = CounsellorSerializer(counsellors, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateCounsellorView(APIView):
    @swagger_auto_schema(
        operation_description="Create a new Counsellor",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['name', 'languages_spoken', 'phone'],
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='Counsellor Name'),
                'languages_spoken': openapi.Schema(type=openapi.TYPE_STRING, description='Languages Spoken'),
                'phone': openapi.Schema(type=openapi.TYPE_STRING, description='Phone Number'),
            }
        ),
        responses={
            201: openapi.Response(description='Counsellor created successfully'),
            400: 'Bad Request',
            401: 'Unauthorized',
            403: 'Forbidden',
            500: 'Internal Server Error',
        },
    )
    def post(self, request):
        serializer = CreateCounsellorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()  # Save the validated data as a new Counsellor
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
