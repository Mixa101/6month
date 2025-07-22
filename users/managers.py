from django.contrib.auth.models import (
    BaseUserManager,
)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username=None, password=None, **kwargs):
        if not email:
            raise ValueError("email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, username=None, password=None, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_active", True)

        if kwargs.get("is_staff") is not True:
            raise ValueError("superuser must be is_staff")

        if kwargs.get("is_superuser") is not True:
            raise ValueError("superuser must be is_superuser")

        if kwargs.get("is_active") is not True:
            raise ValueError("superuser must be is_active")

        return self.create_user(email, username, password, **kwargs)
