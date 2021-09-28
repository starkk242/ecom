from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.base import Model


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager with email as the unique identifier
    """

    def create_user(self, first_name, last_name, email, password, phone_number, ref_code, **extra_fields):
        """
        Create user with the given email and password.
        """
        if not email:
            raise ValueError("The email must be set")
        first_name = first_name.capitalize()
        last_name = last_name.capitalize()
        email = self.normalize_email(email)
        phone_number = phone_number
        ref_code = ref_code

        user = self.model(
            first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, ref_code=ref_code,**extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, first_name, last_name, email, password, **extra_fields):
        """
        Create superuser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(first_name, last_name, email, password,ref_code=" ", **extra_fields)


class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField(max_length=255, verbose_name="First name")
    last_name = models.CharField(max_length=255, verbose_name="Last name")
    email = models.EmailField(unique=True)
    phone_number = models.CharField(null=True,unique=True,max_length=255)
    ref_code = models.CharField(null=True,max_length=7)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name","phone_number"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class ReferalCode(models.Model):
    user = models.ForeignKey(CustomUser, related_name='user', on_delete=models.CASCADE)
    referal_code = models.CharField(max_length=7,blank=True, null=True)
