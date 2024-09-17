from rest_framework import serializers
from .models import Comments
from Post.models import Posts

# Serializer for listing comments with additional fields
class ListCommentsSerial(serializers.ModelSerializer):
    # Adding a custom field for user data using SerializerMethodField

    user = serializers.SerializerMethodField()
    # Using StringRelatedField to represent the post as a string (e.g., __str__ method of the post model)

    post = serializers.StringRelatedField() 

    class Meta:
        model = Comments

    # Defining the fields to be serialized: content, created_at, user, and post

        fields = ('content', 'created_at', 'user', 'post')

    # Custom method to retrieve the username of the user who posted the comment

    def get_user(self, obj):
        return obj.user.username if obj.user else None


class CreatePostSerializer(serializers.ModelSerializer):
    image = serializers.FileField(required=False)

    class Meta:
    # The serializer is tied to the Posts model
     model = Posts
    fields = ('content', 'created_at',  'image')

    def save(self, *args, **kwargs):
            content = self.validated_data.get('content')
            image = self.validated_data.get('image')
                # Accessing the user from the request context (e.g., the user creating the post)
        
            user = self.context['request'].user

