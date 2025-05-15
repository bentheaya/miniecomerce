from django.urls import path
from .views import AddProductView, VerifyProductView

urlpatterns = [
    path('api/products/', AddProductView.as_view(), name='add_product'),
    path('api/products/<int:product_id>/', VerifyProductView.as_view(), name='verify_product'),
]