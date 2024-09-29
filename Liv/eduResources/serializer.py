from rest_framework import serializers
from .models import Eduresources


class CreateEduresourcesSerializer(serializers.ModelSerializer):
    # Making `link` and `resource_type` fields optional for flexibility.
    link = serializers.URLField(required=False)
    resource_type = serializers.ChoiceField(choices=Eduresources.Resource_type.choices, required=False)

    class Meta:
        model = Eduresources
        fields = ('title', 'description', 'link', 'resource_type', 'created_at')

    def save(self, *args, **kwargs):
        title = self.validated_data.get('title')
        description = self.validated_data.get('description')
        link = self.validated_data.get('link', None)
        resource_type = self.validated_data.get('resource_type',
                                                Eduresources.Resource_type.Article)
        user = self.context['request'].user

        eduresource = Eduresources(
            title=title,
            description=description,
            link=link,
            resource_type=resource_type,
            user=user
        )
        eduresource.save()
        return eduresource


class EduReListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Eduresources
        fields = ('user', 'title', 'description', 'link', 'resource_type', 'created_at')
