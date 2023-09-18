from django.db import models


# Create your models here.
class Reservation(models.Model):
    date = models.DateField(null=False)
    time = models.TimeField(null=False)
    customer_name = models.CharField(max_length=100, null=False)
    customer_email = models.EmailField(null=False)
    mentions = models.CharField(max_length=250)
    confirmed = models.BooleanField(default=False)
