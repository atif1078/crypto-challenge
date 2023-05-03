from django.db import models

# Create your models here.
class Price(models.Model):
    currency_name = models.CharField(max_length=255)
    current_price = models.DecimalField(max_digits=20, decimal_places=10)
    price_1h_ago = models.DecimalField(max_digits=20, decimal_places=10)
    price_4h_ago = models.DecimalField(max_digits=20, decimal_places=10)
    price_8h_ago = models.DecimalField(max_digits=20, decimal_places=10)
    price_24h_ago = models.DecimalField(max_digits=20, decimal_places=10)
    up_by = models.DecimalField(max_digits=20, decimal_places=10)
    time = models.DateTimeField()
    date = models.DateTimeField()