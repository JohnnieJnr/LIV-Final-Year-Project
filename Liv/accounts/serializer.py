from rest_framework import serializers

from .models import Account


class AccountRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = Account
        fields = ['last_name', 'first_name', 'email', 'phone', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = Account(email=self.validated_data['email'])
        user.first_name = self.validated_data['first_name']
        user.last_name = self.validated_data['last_name']
        user.phone = self.validated_data['phone']
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('last_name', 'first_name', 'email', 'phone', 'username', 'date_joined', 'last_login', 'is_active', 'is_admin')


class AccountDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', 'phone')
        read_only_fields = ('email',)
