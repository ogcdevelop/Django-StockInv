from django.db import models
from django.utils import timezone

class Product(models.Model):
    PRODUCT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('N', 'NA'),
    )

    PRODUCT_COLOURS = (
        ('B', 'Black'),
        ('W', 'White'),
        ('L', 'Blue'),
        ('E', 'Grey'),
        ('G', 'Green'),
    )

    name = models.CharField(max_length=64)
    code = models.CharField(max_length=15, default="")
    description = models.TextField()
    standard_price = models.DecimalField(max_digits=6, blank=True, null=True, decimal_places=1)
    list_price = models.DecimalField(max_digits=6, blank=True, null=True, decimal_places=1)
    purchase_date = models.DateTimeField(blank=True, null=True)
    expiry_date = models.DateTimeField(blank=True, null=True)
    qty = models.FloatField(default=0.0)
    min_qty = models.FloatField(default=0.0)
    max_qty = models.FloatField(default=0.0)
    pic_l = models.ImageField(upload_to="products", null=True)
    pic_s = models.ImageField(upload_to="products", null=True)
    product_size = models.CharField(max_length=1, choices=PRODUCT_SIZES)
    colour = models.CharField(max_length=1, choices=PRODUCT_COLOURS)
    weight = models.DecimalField(max_digits=6, blank=True, null=True, decimal_places=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(default="")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    class Meta:
        ordering = ('name',)
