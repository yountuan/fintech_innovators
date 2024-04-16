from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, AccountViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'accounts', AccountViewSet)

urlpatterns = [
    path('', include(router.urls)),
]