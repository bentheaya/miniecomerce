from django.db import models

class Order(models.Model):
    user_id = models.PositiveIntegerField()
    product_id = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by User {self.user_id}"
