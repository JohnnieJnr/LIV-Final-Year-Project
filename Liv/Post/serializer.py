from rest_framework import serializers
from .models import Posts


class ListPostSerial(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Posts
        fields = ('content', 'created_at', 'user', 'image')

        def get_user(self, obj):
            return obj.user.last_name if obj.user else None


class CreatePostSerializer(serializers.ModelSerializer):
    image = serializers.FileField()

    class Meta:
        model = Posts
        fields = ('content', 'created_at', 'user', 'image')

        def save(self, *args, **kwargs):
            content = self.validated_data.get('content')
            image = self.validated_data.get('image')
            user = self.validated_data.get('user')

