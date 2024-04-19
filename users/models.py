from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email field is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        user = self._create_user(email, password, **extra_fields)
        return user


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    customer_name = models.CharField(max_length=30)
    card_id = models.IntegerField(null=True)
    total_balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.customer_name
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    


class Account(models.Model):
    """Accounts Database Table"""

    id = models.BigAutoField(primary_key=True)
    customer_name = models.ForeignKey(User, on_delete=models.CASCADE)
    card_id = models.CharField(max_length=20, unique=True)
    total_balance = models.DecimalField(max_digits=10, decimal_places=2)
    available_balance = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.card_id 
    
    def save(self, *args, **kwargs):
        # Automatically bind card_id from related user to account
        if not self.card_id:
            self.card_id = self.customer_name.card_id
        super().save(*args, **kwargs)


class JWTToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)  # JWT Токен
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

