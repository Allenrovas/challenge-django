# Django Coding Challenge

## Setup

Clone this repository using GIT. I recommend you use Github Desktop or VS Code (see point 1 in Development)

To run this project you need to install any recent version of Python. Preferably Python 3.9+ After that you are advised to create a virtual environment so that your dependencies are contained within the workspace. **On Windows, make sure to add Python to your PATH, you may need to logout or reboot to run python**

Once you have Python installed and working, you can install the project dependencies by running `pip install -r requirements.txt`. This will install everything for you, then you can run migrations with `python manage.py migrate` (make sure to run this command within the nimblestore directory). If successful you should see a new file called `db.sqlite3` in your work directory.

Lastly you should be able to run the server with `python manage.py runserver` which will let you see a very basic webpage in https://127.0.0.1:8000 (Open this link in your browser), this page will help you test your work, I recommend you open the web inspector and switch to the network tab to see what is happening. If you want you can find the source for this page in the `nimblestore/checkout/templates/index.html` file. You do NOT need to edit anything on it.

## Development

Here are some general guides and also some tips:

1. Install VS Code (optional) [here](https://code.visualstudio.com/)
2. Install recommended extensions (Python, SonarLint)
3. Use Google as much as you need to, find official sources and documentations, examples and tutorials are good sources.
4. You CAN use AI, in fact I encourage you to do so.

Once you start creating models, you will need to create and run migrations, the commands you'll need are:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Documentation

- **Docstrings**: Please provide docstrings for your functions and classes using the [Google style guide](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html). This helps others understand the purpose and usage of your code.
- **README**: Update the README file to include instructions on how to set up and run the project, as well as any other relevant information. This ensures that anyone who uses your project can easily get started.

## Unit Tests

- **Unit Tests with pytest**: Write unit tests for your code using `pytest`. Ensure you cover different scenarios, including edge cases.
  To run your tests, use the command:
  ```bash
  pytest
  ```
  Create a `tests` directory in your project and add your test files there. Follow the convention of naming your test files starting with `test_`.

## Pre-commit Hooks

- **Pre-commit**: Install `pre-commit` to ensure code quality before commits. Pre-commit hooks can automatically format your code and run tests before each commit. `pre-commit` should have been installed by the previous commmands, yet you still have to run the following:
  Initialize the pre-commit hooks with:
  ```bash
  pre-commit install
  ```
  Now, every time you make a commit, `pre-commit` will run the defined hooks to ensure code quality.

## Problem Statement

Your company has a Django application that stores product information. Each product has a name, price, and quantity available. Your task is to create three API endpoints:

1. `GET /api/products/`: This endpoint should return a list of all products, with each product's name, price, and quantity available.

2. `POST /api/order/`: This endpoint should accept a list of products and quantities, calculate the total cost of the order, and return it. If a product doesn't exist or there isn't enough quantity available, it should return an appropriate error message.

3. `PUT /api/products/<id>/` or `PATCH /api/products/<id>/`: These endpoints should allow for editing the details of a product. The `PUT` method should update all fields of the product, while the `PATCH` method should allow partial updates.

You can search globally for `TODO` to find the files you must edit to complete this assignment.

Good Luck,
Juan Mora



# SOLUTION AND GUIDE

## Index

-[Setup Envoriment](#setup-envoriment)

-[Create Models](#create-models)

-[Create Views](#create-views)

-[Update URLs](#update-urls)

-[Test the API](#test-the-api)


## Setup Envoriment

First of all, you need to clone this repository using GIT.

```bash
git clone https://github.com/JPaulMora/django-coding-challenge
```

Navigate to the project directory

```bash
cd nimblestore
```

Create a virtual environment and activate it

```bash
python -m venv venv
# On Windows
venv/bin/activate
# On Linux
source venv/Scripts/activate
```

Install the project dependencies

```bash
pip install -r requirements.txt
```

Run the migrations

```bash
python manage.py migrate
```

Start the server

```bash
python manage.py runserver
```

## Create Models

The first thing we need to do is create the models for the products. We will create a model called `Product` with the following fields:

- `name`: The name of the product
- `price`: The price of the product
- `quantity`: The quantity available of the product

Create a new file called `models.py` in the `products` app directory and add the following code:

```python
from django.db import models

class Product(models.Model):
    """
    Model representing a product.

    Attributes:
        name (str): The name of the product.
        price (Decimal): The price of the product.
        quantity (int): The available quantity of the product.
    """
    name = models.CharField(max_length=100, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        """
        Return a string representation of the product.

        Returns:
            str: The name of the product.
        """
        return self.name
```

Next, we need to create a serializer for the `Product` model. Create a new file called `serializers.py` in the `products` app directory and add the following code:

```python
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.

    Attributes:
        model (Product): The Product model that the serializer works with.
        fields (list): The fields from the Product model that should be included in the serialized representation.
    """
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'quantity']
```

Now we need make and apply the migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## Create Views

Now that we have the models and serializers in place, we can create the views for the API endpoints. We will create a view for each of the three API endpoints mentioned in the problem statement.

Create a new file called `views.py` in the `products` app directory and add the following code:

```python
# Django Coding Challenge

## Setup

Clone this repository using GIT. I recommend you use Github Desktop or VS Code (see point 1 in Development)

To run this project you need to install any recent version of Python. Preferably Python 3.9+ After that you are advised to create a virtual environment so that your dependencies are contained within the workspace. **On Windows, make sure to add Python to your PATH, you may need to logout or reboot to run python**

Once you have Python installed and working, you can install the project dependencies by running `pip install -r requirements.txt`. This will install everything for you, then you can run migrations with `python manage.py migrate` (make sure to run this command within the nimblestore directory). If successful you should see a new file called `db.sqlite3` in your work directory.

Lastly you should be able to run the server with `python manage.py runserver` which will let you see a very basic webpage in https://127.0.0.1:8000 (Open this link in your browser), this page will help you test your work, I recommend you open the web inspector and switch to the network tab to see what is happening. If you want you can find the source for this page in the `nimblestore/checkout/templates/index.html` file. You do NOT need to edit anything on it.

## Development

Here are some general guides and also some tips:

1. Install VS Code (optional) [here](https://code.visualstudio.com/)
2. Install recommended extensions (Python, SonarLint)
3. Use Google as much as you need to, find official sources and documentations, examples and tutorials are good sources.
4. You CAN use AI, in fact I encourage you to do so.

Once you start creating models, you will need to create and run migrations, the commands you'll need are:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Documentation

- **Docstrings**: Please provide docstrings for your functions and classes using the [Google style guide](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html). This helps others understand the purpose and usage of your code.
- **README**: Update the README file to include instructions on how to set up and run the project, as well as any other relevant information. This ensures that anyone who uses your project can easily get started.

## Unit Tests

- **Unit Tests with pytest**: Write unit tests for your code using `pytest`. Ensure you cover different scenarios, including edge cases.
  To run your tests, use the command:
  ```bash
  pytest
  ```
  Create a `tests` directory in your project and add your test files there. Follow the convention of naming your test files starting with `test_`.

## Pre-commit Hooks

- **Pre-commit**: Install `pre-commit` to ensure code quality before commits. Pre-commit hooks can automatically format your code and run tests before each commit. `pre-commit` should have been installed by the previous commmands, yet you still have to run the following:
  Initialize the pre-commit hooks with:
  ```bash
  pre-commit install
  ```
  Now, every time you make a commit, `pre-commit` will run the defined hooks to ensure code quality.

## Problem Statement

Your company has a Django application that stores product information. Each product has a name, price, and quantity available. Your task is to create three API endpoints:

1. `GET /api/products/`: This endpoint should return a list of all products, with each product's name, price, and quantity available.

2. `POST /api/order/`: This endpoint should accept a list of products and quantities, calculate the total cost of the order, and return it. If a product doesn't exist or there isn't enough quantity available, it should return an appropriate error message.

3. `PUT /api/products/<id>/` or `PATCH /api/products/<id>/`: These endpoints should allow for editing the details of a product. The `PUT` method should update all fields of the product, while the `PATCH` method should allow partial updates.

You can search globally for `TODO` to find the files you must edit to complete this assignment.

Good Luck,
Juan Mora



# SOLUTION AND GUIDE

## Index

-[Setup Envoriment](#setup-envoriment)
-[Create Models](#create-models)
-[Create Views](#create-views)


## Setup Envoriment

First of all, you need to clone this repository using GIT.

```bash
git clone https://github.com/JPaulMora/django-coding-challenge
```

Navigate to the project directory

```bash
cd nimblestore
```

Create a virtual environment and activate it

```bash
python -m venv venv
# On Windows
venv/bin/activate
# On Linux
source venv/Scripts/activate
```

Install the project dependencies

```bash
pip install -r requirements.txt
```

Run the migrations

```bash
python manage.py migrate
```

Start the server

```bash
python manage.py runserver
```

## Create Models

The first thing we need to do is create the models for the products. We will create a model called `Product` with the following fields:

- `name`: The name of the product
- `price`: The price of the product
- `quantity`: The quantity available of the product

Create a new file called `models.py` in the `products` app directory and add the following code:

```python
from django.db import models

class Product(models.Model):
    """
    Model representing a product.

    Attributes:
        name (str): The name of the product.
        price (Decimal): The price of the product.
        quantity (int): The available quantity of the product.
    """
    name = models.CharField(max_length=100, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        """
        Return a string representation of the product.

        Returns:
            str: The name of the product.
        """
        return self.name
```

Next, we need to create a serializer for the `Product` model. Create a new file called `serializers.py` in the `products` app directory and add the following code:

```python
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.

    Attributes:
        model (Product): The Product model that the serializer works with.
        fields (list): The fields from the Product model that should be included in the serialized representation.
    """
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'quantity']
```

Now we need make and apply the migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## Create Views

Now that we have the models and serializers in place, we can create the views for the API endpoints. We will create a view for each of the three API endpoints mentioned in the problem statement.

Create a new file called `views.py` in the `products` app directory and add the following code:

```python
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated  # Ensure to import IsAuthenticated if authentication is required
from django.views import generic

class IndexView(generic.TemplateView):
    """
    View for rendering the index.html template.

    Attributes:
        template_name (str): The name of the template to render.
    """
    template_name = "index.html"

class ProductListView(viewsets.ModelViewSet):
    """
    ViewSet for managing Product objects.

    This view supports listing, creating, updating, and partial updating products.

    Attributes:
        queryset (QuerySet): The queryset of Product objects.
        serializer_class (class): The serializer class used for Product serialization.
        permission_classes (list): The permission classes applied to this view.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]  

    def list(self, request):
        """
        Retrieve a list of all products.

        Returns:
            Response: A response containing serialized data of all products.
        """
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        Create a new product.

        Args:
            request (Request): The HTTP POST request containing product data.

        Returns:
            Response: A response with serialized data of the created product or errors.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk=None):
        """
        Update an existing product.

        Args:
            request (Request): The HTTP PUT request containing updated product data.
            pk (int): The primary key of the product to update.

        Returns:
            Response: A response with serialized data of the updated product or errors.
        """
        product = self.get_object()
        serializer = self.serializer_class(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        """
        Partially update an existing product.

        Args:
            request (Request): The HTTP PATCH request containing partial product data.
            pk (int): The primary key of the product to partially update.

        Returns:
            Response: A response with serialized data of the updated product or errors.
        """
        product = self.get_object()
        serializer = self.serializer_class(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderView(APIView):
    """
    View for creating orders for products.

    This view handles the creation of orders based on incoming order data.

    Attributes:
        permission_classes (list): The permission classes applied to this view.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Handle POST requests to create orders.

        Args:
            request (Request): The HTTP POST request containing order data.

        Returns:
            Response: A response with the total cost of the order or error messages.
        """
        order_items = request.data
        total = 0

        for item in order_items:
            try:
                product_name = item.get("product")
                quantity = int(item.get("quantity"))

                product = Product.objects.get(name=product_name)

                if product.quantity < quantity:
                    return Response({"error": f"Not enough stock for {product.name}"}, status=status.HTTP_400_BAD_REQUEST)

                total += product.price * quantity
                product.quantity -= quantity
                product.save()
            except Product.DoesNotExist:
                return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
            except ValueError as ve:
                return Response({"error": str(ve)}, status=status.HTTP_400_BAD_REQUEST)

        response_obj = {"total": total}
        return Response(response_obj)
```

## Update URLs

Finally, we need to update the `urls.py` file in the `products` app directory to include the URLs for the API endpoints.

Add the following code to the `urls.py` file:

```python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("api", views.IndexView.as_view(), name="index"),
     path("api/products/", views.ProductListView.as_view({"get": "list", "post": "create"}), name="products"),
    path("api/products/<int:pk>/", views.ProductListView.as_view({"put": "update", "patch": "partial_update"}), name="product-detail"),
    path("api/order/", views.OrderView.as_view(), name="order"),
]
```

Now you should be able to access the API endpoints at the following URLs:

- `GET /api/products/`: List all products
- `POST /api/products/`: Create a new product
- `PUT /api/products/<id>/`: Update a product
- `PATCH /api/products/<id>/`: Partially update a product
- `POST /api/order/`: Create an order

## Test the API

You can test the API endpoints using pytest and Django's test client. Create a new file called `test_views.py` in the `checkout` app directory and add the following code:

```python
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from checkout.models import Product  # Make sure to import the correct model
from checkout.serializers import ProductSerializer  # Import your serializer

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

    response = api_client.post(url, order_data, format='json')

    assert response.status_code == 200
    assert 'total' in response.data
    assert response.data['total'] == 65.00  

    product1.refresh_from_db()
    product2.refresh_from_db()
    assert product1.quantity == 98  # 100 - 2
    assert product2.quantity == 197  # 200 - 3
```

You can run the tests using the following command:

```bash
pytest
```

This will run the test cases and verify that the API endpoints are working correctly.

That's it! You have now created a Django API with the required endpoints for managing products and orders. You can further customize the views, serializers, and models to add more functionality as needed.
