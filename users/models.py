from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.crypto import get_random_string




class User(AbstractUser):
    email = models.EmailField(unique=True)
    customer_name = models.CharField(max_length=30)
    card_id = models.IntegerField()
    total_balance = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)

    def __str__(self):
        return self.customer_name


class Account(models.Model):
    """Accounts Database Table"""

    id = models.BigAutoField(primary_key=True)
    customer_name = models.ForeignKey(User, on_delete=models.CASCADE)
    card_id = models.CharField(max_length=20, unique=True)
    currency = models.CharField(max_length=3)
    total_balance = models.DecimalField(max_digits=10, decimal_places=2)
    available_balance = models.DecimalField(max_digits=10, decimal_places=2)
    reserved_amount = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.card_id 


class JWTToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)  # JWT Токен
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()