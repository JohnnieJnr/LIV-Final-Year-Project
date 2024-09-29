from rest_framework import serializers
from .models import Counsellor


class CounsellorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counsellor
        fields = ['name', 'languages_spoken', 'phone']


class CreateCounsellorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counsellor
        fields = ['name', 'languages_spoken', 'phone']

    def save(self, *args, **kwargs):
        name = self.validated_data.get('name')
        languages_spoken = self.validated_data.get('languages_spoken')
        phone = self.validated_data.get('phone')

        counsellor = Counsellor(
            name=name,
            languages_spoken=languages_spoken,
            phone=phone
        )

        counsellor.save()

        return counsellor
