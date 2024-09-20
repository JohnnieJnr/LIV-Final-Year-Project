from rest_framework import serializers
from .models import Posts


class ListPostSerial(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Posts
        fields = ('content', 'created_at', 'user', 'image')

    def get_user(self, obj):
        return obj.user.username if obj.user else None


class CreatePostSerializer(serializers.ModelSerializer):
    image = serializers.FileField(required=False)

    class Meta:
        model = Posts

        fields = ('content', 'created_at', 'image')

        def save(self, *args, **kwargs):
            content = self.validated_data.get('content')
            image = self.validated_data.get('image')
            user = self.context['request'].user
