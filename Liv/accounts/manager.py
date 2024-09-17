from django.contrib.auth.base_user import BaseUserManager


class MyAccountManager(BaseUserManager):
        # Method to create a regular user
    def create_user(self, first_name, last_name, email, phone, password=None):
                # Ensure that an email is provided, raise an error if it's missing
        if not email:
            raise ValueError('User must have an email address')

        # Create a new user instance with the given data and normalize the email
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
        )
                # Set the user's password (this automatically hashes the password)
        user.set_password(password)
                # Save the user to the database using the current database instance
        user.save(using=self._db)
        return user # Return the created user instance

    def create_superuser(self, first_name, last_name, email, phone, password, **kwargs):
                # Create a regular user first by calling create_user
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            **kwargs  # Any additional keyword arguments can be passed

        )
                # Assign the superuser permissions to the user
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
                # Save the superuser to the database
        user.save(using=self._db)
        return user  # Return the created superuser instance
