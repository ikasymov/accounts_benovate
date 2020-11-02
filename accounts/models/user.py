from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import UserManager


class MainUser(AbstractUser):
    ident_code = models.IntegerField(unique=True)

    REQUIRED_FIELDS = ['ident_code']

    objects = UserManager()

    @staticmethod
    def exist_balance(balance, amount):
        return balance >= amount
