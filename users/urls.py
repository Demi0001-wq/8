from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .apps import UsersConfig
from .views import (
    UserCreateAPIView, UserListAPIView, UserRetrieveAPIView,
    UserUpdateAPIView, UserDestroyAPIView, PaymentListAPIView,
    PaymentCreateAPIView, PaymentStatusAPIView
)

app_name = UsersConfig.name

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('list/', UserListAPIView.as_view(), name='user-list'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user-detail'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user-delete'),

    # Payments
    path('payments/', PaymentListAPIView.as_view(), name='payment-list'),
    path('payments/create/', PaymentCreateAPIView.as_view(), name='payment-create'),
    path('payments/status/<int:pk>/', PaymentStatusAPIView.as_view(), name='payment-status'),
]
