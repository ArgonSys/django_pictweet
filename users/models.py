from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.utils import timezone
from django.db import models

class User(AbstractBaseUser, PermissionsMixin):
    username_validator = ASCIIUsernameValidator()
    username = models.CharField(
        "ユーザー名",
        max_length=150,
        unique=False,
        validators=[username_validator],
    )

    email = models.EmailField(
        "メールアドレス",
        unique=True,
        error_messages={
            "unique": "Email address has already token",
        },
    )

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(
        "staff status",
        default=False,
    )
    is_active = models.BooleanField(
        "active",
        default=True,
    )
    date_joined = models.DateTimeField("date joined", default=timezone.now)


    objects = UserManager()


    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'
