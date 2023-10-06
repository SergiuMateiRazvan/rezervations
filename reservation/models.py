from django.db import models


# Create your models here.
class Reservation(models.Model):
    date = models.DateField(null=False)
    time = models.CharField(null=False, max_length=5)
    customer_name = models.CharField(max_length=100, null=False)
    customer_email = models.EmailField(null=False)
    customer_phone = models.CharField(max_length=12, null=False)
    mentions = models.CharField(max_length=250, null=True)
    no_persons = models.IntegerField(null=False)
    confirmed = models.BooleanField(default=False)
