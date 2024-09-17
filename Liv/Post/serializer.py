from rest_framework import serializers
from .models import Posts


class ListPostSerial(serializers.ModelSerializer):
        # Define a custom field to include the username of the user who created the post
    user = serializers.SerializerMethodField()

    # Meta class to define the model and fields to be serialized
    class Meta:
        model = Posts   # Use the Posts model
        
                # Specify the fields that will be included in the serialized output
        fields = ('content', 'created_at', 'user', 'image')

    # Method to retrieve the username of the user who created the post
    def get_user(self, obj):
                # If the post has a user associated, return the user's username; otherwise, return None
        return obj.user.username if obj.user else None


class CreatePostSerializer(serializers.ModelSerializer):
        # Optional field for uploading an image with the post
    image = serializers.FileField(required=False)

    class Meta:
        model = Posts  # Use the Posts model

                # Specify the fields that can be provided when creating a post
        fields = ('content', 'created_at',  'image')

        def save(self, *args, **kwargs):
                    # Retrieve the content of the post from the validated data
            content = self.validated_data.get('content')
                    # Retrieve the image of the post from the validated data, if provided
            image = self.validated_data.get('image')
                    # Retrieve the user making the request (this is passed through the request context)
            user = self.context['request'].user

