import pytest
from django.test import Client
from .models import Order

@pytest.mark.django_db
def test_create_order():
    client = Client()
    response = client.post('/orders/', {
        "user_id": 1,
        "item_ids": [101, 102, 103],
        "total_amount": 150.00
    }, content_type="application/json")
    assert response.status_code == 201

@pytest.mark.django_db
def test_order_status():
    order = Order.objects.create(user_id=1, item_ids=[101, 102], total_amount=100)
    client = Client()
    response = client.get(f'/orders/{order.id}/')
    assert response.status_code == 200
    assert response.json()["status"] == "Pending"
