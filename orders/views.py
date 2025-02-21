from django.shortcuts import render
from django.db.models import Count, Avg, ExpressionWrapper, F, fields
from rest_framework.generics import GenericAPIView
from orders.mixins import BaseApiMixin
from orders.tasks import process_order
from orders.constants import StatusChoices
from orders.models import Order
from orders.types import OrderRequestEntity

# Create your views here.


class OrdersView(GenericAPIView, BaseApiMixin):

    def post(self, request):
        data = request.data
        data: OrderRequestEntity = OrderRequestEntity(**data)
        order = Order.objects.create(order_id=data.order_id, user_id=data.user_id, item_ids=data.item_ids, total_amount=data.total_amount, status=StatusChoices.PENDING)
        process_order.delay(data.order_id)
        return self.success_response(data={"order_id": data.order_id, "status": StatusChoices.PENDING})
    

    def get(self, request):
        orders = Order.objects.all()
        return self.success_response(data=orders)
    

class MetricsViewSet(GenericAPIView, BaseApiMixin):
    
    def get(self, request):
        total_orders = Order.objects.count()
        avg_processing_time = Order.objects.filter(status="Completed").annotate(
            processing_time=ExpressionWrapper(F("updated_at") - F("created_at"), output_field=fields.DurationField())
        ).aggregate(avg_time=Avg("processing_time"))["avg_time"]
        avg_processing_time_seconds = avg_processing_time.total_seconds() if avg_processing_time else 0
        status_counts = Order.objects.values("status").annotate(count=Count("status"))

        return self.success_response(data={
            "total_orders": total_orders,
            "avg_processing_time": avg_processing_time_seconds,
            "status_counts": {entry["status"]: entry["count"] for entry in status_counts}
        })
    


    