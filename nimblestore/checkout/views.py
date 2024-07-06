from django.views import generic
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer


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
                    return Response(
                        {"error": f"Not enough stock for {product.name}"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                total += product.price * quantity
                product.quantity -= quantity
                product.save()
            except Product.DoesNotExist:
                return Response(
                    {"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND
                )
            except ValueError as ve:
                return Response({"error": str(ve)}, status=status.HTTP_400_BAD_REQUEST)

        response_obj = {"total": total}
        return Response(response_obj)
