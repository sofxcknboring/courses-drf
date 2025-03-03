from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import PaymentViewSet
from users.apps import UsersConfig

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'', PaymentViewSet, basename='payment')

urlpatterns = [
    path('', include(router.urls)),
]