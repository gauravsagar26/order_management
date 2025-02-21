from django.urls import path
from orders.views import OrdersView, MetricsViewSet

urlpatterns = [
    path('orders/', OrdersView.as_view(), name='orders'),
    path('metrics/', MetricsViewSet.as_view(), name='metrics'),
]