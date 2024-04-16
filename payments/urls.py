from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionsViewSet, TransfersViewSet

router = DefaultRouter()
router.register(r'transactions', TransactionsViewSet)
router.register(r'transfers', TransfersViewSet)

urlpatterns = [
    path('', include(router.urls)),
]