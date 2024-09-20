from rest_framework import serializers

from .models import Account


class AccountRegistrationSerializer(serializers.ModelSerializer):
    # Adding a second password field for confirmation, styled as a password input and write-only

    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        # The serializer is tied to the Account model

        model = Account

        # Fields that will be accepted during registration: last name, first name, email, phone, password, and password confirmation
        fields = ['last_name', 'first_name', 'email', 'phone', 'password', 'password2']

        # Extra settings for the password field to ensure it's write-only and won't be displayed in responses
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        # Creating a new Account instance using the validated email data
        user = Account(email=self.validated_data['email'])
        user.first_name = self.validated_data['first_name']
        user.last_name = self.validated_data['last_name']
        user.phone = self.validated_data['phone']
        # Retrieving the password and confirmation password from the validated data
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        # Checking if both passwords match, if not, raise a validation error
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})

            # Set the user's password using Django's set_password method (handles hashing)
        user.set_password(password)

        # Save the new user to the database
        user.save()
        return user


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        # The serializer is tied to the Account model
        model = Account
        # Fields to be serialized: general account information including first name, last name, email, phone, and account metadata (date joined, last login, etc.)
        fields = (
        'last_name', 'first_name', 'email', 'phone', 'username', 'date_joined', 'last_login', 'is_active', 'is_admin')


class AccountDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', 'phone')
        read_only_fields = ('email',)
