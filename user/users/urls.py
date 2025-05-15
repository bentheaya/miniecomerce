from django.urls import path
from .views import RegisterView, VerifyUserView

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/users/verify/<int:user_id>/', VerifyUserView.as_view(), name='verify_user'),
]