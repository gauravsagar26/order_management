from celery import shared_task
import time
from orders.models import Order

@shared_task
def process_order(order_id):
    try:
        order = Order.objects.get(id=order_id)
        order.status = "Processing"
        order.save()

        time.sleep(2)  # Simulating processing delay

        order.status = "Completed"
        order.save()
        return f"Order {order_id} processed."
    except Order.DoesNotExist:
        return f"Order {order_id} not found."