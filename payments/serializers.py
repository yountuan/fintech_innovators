from rest_framework import serializers
from .models import Transactions, Transfers




class WebhookSerializer(serializers.Serializer):
    """Serializer for checking recieved data format from scheme webhook"""

    card_id = serializers.CharField(max_length=16)
    transaction_id = serializers.CharField(max_length=16)
    merchant_name = serializers.CharField(max_length=255)
    merchant_country = serializers.CharField(max_length=4)
    merchant_city = serializers.CharField(max_length=128, required=False)
    billing_amount = serializers.DecimalField(max_digits=11, decimal_places=2)
    transaction_amount = serializers.DecimalField(max_digits=11, decimal_places=2)
    transaction_currency = serializers.CharField(max_length=3)


class TransactionsSerializer(serializers.Serializer):
    """Serializer for checking format of data recieved through URL parameters"""

    cardholder = serializers.IntegerField()
    start_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    end_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')


class BalancesSerializer(serializers.Serializer):
    """Serializer for checking format of data recieved through URL parameters"""

    cardholder = serializers.IntegerField()
