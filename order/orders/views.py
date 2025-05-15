from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer
import requests

class CreateOrderView(APIView):
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user_id = serializer.validated_data['user_id']
        product_id = serializer.validated_data['product_id']
        quantity = serializer.validated_data['quantity']

        # Verify user exists
        try:
            user_response = requests.get(f'http://user-service:8001/api/users/verify/{user_id}/')
            if user_response.status_code != 200:
                return Response({"error": "Invalid user"}, status=status.HTTP_400_BAD_REQUEST)
        except requests.RequestException:
            return Response({"error": "User service unavailable"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        # Verify product exists and get price
        try:
            product_response = requests.get(f'http://product-service:8002/api/products/{product_id}/')
            if product_response.status_code != 200:
                return Response({"error": "Invalid product"}, status=status.HTTP_400_BAD_REQUEST)
            product_data = product_response.json()
            if product_data['data']['stock'] < quantity:
                return Response({"error": "Insufficient stock"}, status=status.HTTP_400_BAD_REQUEST)
            price = product_data['data']['price']
        except requests.RequestException:
            return Response({"error": "Product service unavailable"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        # Calculate total price
        serializer.validated_data['total_price'] = float(price) * quantity

        # Save order
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)