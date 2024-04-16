from django.contrib import admin
from .models import Transactions, Transfers

# Register your models here.
admin.site.register(Transactions)
admin.site.register(Transfers)