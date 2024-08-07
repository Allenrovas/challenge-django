from django.db import models


class Product(models.Model):
    """
    Model representing a product.

    Attributes:
        name (str): The name of the product.
        price (Decimal): The price of the product.
        quantity (int): The available quantity of the product.
    """

    name = models.CharField(max_length=100, default="")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        """
        Return a string representation of the product.

        Returns:
            str: The name of the product.
        """
        return self.name
