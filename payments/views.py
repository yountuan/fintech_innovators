from rest_framework import viewsets
from .models import Transactions, Transfers
from .serializers import TransactionsSerializer, TransfersSerializer

class TransactionsViewSet(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer

class TransfersViewSet(viewsets.ModelViewSet):
    queryset = Transfers.objects.all()
    serializer_class = TransfersSerializer