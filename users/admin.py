from django.contrib import admin
from .models import User, JWTToken

# Register your models here.
admin.site.register(User)
admin.site.register(JWTToken)