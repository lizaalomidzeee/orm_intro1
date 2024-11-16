# inventory/models.py
from django.db import models

class InventoryItem(models.Model):
    name = models.CharField(max_length=100)  # Product name (text field)
    description = models.TextField()  # Product description (text field)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price (decimal field)
    stock = models.IntegerField()  # Stock (integer field)

    def __str__(self):
        return self.name
