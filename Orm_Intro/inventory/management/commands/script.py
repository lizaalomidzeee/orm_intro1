from django.core.management import BaseCommand
from inventory.models import Product

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        products = Product.objects.filter(name__icontains="phone")
        print(products)
        
        # laptop = Product.objects.filter(name__iexact="Laptop")
        # print(laptop)
        
        # tv = Product.objects.filter(name__exact="TV")
        # print(tv)
        
        # high_quality = Product.objects.filter(description__contains="high quality")
        # print(high_quality)
        
        # expensive_products = Product.objects.filter(price__gt=500)
        # print(expensive_products)
        
        # cheap_products = Product.objects.filter(price__lt=100)
        # print(cheap_products)
        
        # in_stock = Product.objects.filter(stock__gte=10)
        # print(in_stock)
        
        # low_stock = Product.objects.filter(stock__lte=5)
        # print(low_stock)
        
        # mid_range_products = Product.objects.filter(price__range=(100, 300))
        # print(mid_range_products)
        
        # pro_products = Product.objects.filter(name__startswith="Pro")
        # print(pro_products)
        
        # x_ending_products = Product.objects.filter(name__endswith="X")
        # print(x_ending_products)
        
        # no_description = Product.objects.filter(description__isnull=True)
        # print(no_description)
        
        
        # not_expensive = Product.objects.exclude(price__gt=200)
        # print(not_expensive) 
        
        # specific_products = Product.objects.filter(price__gt=50, stock__lt=5)
        # print(specific_products) 
        
        # camera_products = Product.objects.filter(name="Camera", price__lt=300)
        # print(camera_products)