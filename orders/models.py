from django.db import models

# Create your models here.


from django.db import models

from orders.constants import StatusChoices



class Order(models.Model):
    order_id = models.CharField(max_length=50, unique=True)
    user_id = models.IntegerField()
    item_ids = models.JSONField()  # Stores a list of item IDs
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    