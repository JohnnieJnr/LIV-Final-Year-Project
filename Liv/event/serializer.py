from .models import Events
from rest_framework import serializers


class EventListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Events
        fields = ('user', 'event_name', 'description', 'event_date', 'event_location', 'created_at')


class CreateEventsSerializer(serializers.ModelSerializer):
    image = serializers.FileField(required=False)

    class Meta:
        model = Events

        fields = ('event_name', 'description',  'event_date', 'image', 'event_location', 'created_at')

        def save(self, *args, **kwargs):
            event_name = self.validated_data.get('event_name')
            description = self.validated_data.get('description')
            event_date = self.validated_data.get('event_date')
            event_location = self.validated_data.get('event_location')
            image = self.validated_data.get('image')
            user = self.context['request'].user
