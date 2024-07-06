import pytest
from checkout.models import Product  # Make sure to import the correct model
from checkout.serializers import ProductSerializer  # Import your serializer
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    """
    Fixture that provides an instance of APIClient for testing.
    """
    return APIClient()


@pytest.fixture
def create_product():
    """
    Fixture that creates a Product instance with specified attributes.
    """

    def _create_product(name, price, quantity):
        return Product.objects.create(name=name, price=price, quantity=quantity)

    return _create_product


@pytest.mark.django_db
def test_get_products(api_client, create_product):
    """
    Test case to verify GET request for retrieving products.
    """
    product1 = create_product("Test Product 1", 10.00, 100)
    product2 = create_product("Test Product 2", 15.00, 200)

    url = reverse("products")  # Adjust this to the actual URL name

    response = api_client.get(url)
    assert response.status_code == 200

    serializer = ProductSerializer([product1, product2], many=True)
    assert response.data == serializer.data


@pytest.mark.django_db
def test_post_order(api_client, create_product):
    """
    Test case to verify POST request for placing an order.
    """
    product1 = create_product("Test Product 1", 10.00, 100)
    product2 = create_product("Test Product 2", 15.00, 200)

    order_data = [
        {"product": product1.name, "quantity": 2},
        {"product": product2.name, "quantity": 3},
    ]

    url = reverse("order")  # Adjust this to the actual URL name

    response = api_client.post(url, order_data, format="json")

    assert response.status_code == 200
    assert "total" in response.data
    assert response.data["total"] == 65.00

    product1.refresh_from_db()
    product2.refresh_from_db()
    assert product1.quantity == 98  # 100 - 2
    assert product2.quantity == 197  # 200 - 3
