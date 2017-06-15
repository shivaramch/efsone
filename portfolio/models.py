from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    cust_number = models.AutoField(max_length=5, primary_key=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    email = models.CharField(max_length=200)
    cell_phone = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(
        blank=True, null=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Investment(models.Model):
    category = models.CharField(max_length=50)
    # name = models.CharField('portfolio.Customer')
    description = models.CharField(max_length=200)
    cust_number = models.ForeignKey('portfolio.Customer')
    acquired_value = models.DecimalField(max_digits=10, decimal_places=2)
    acquired_date = models.DateTimeField(default=timezone.now)
    recent_value = models.DecimalField(max_digits=10, decimal_places=2)
    recent_date = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def created(self):
        self.acquired_date = timezone.now()
        self.save()

    def updated(self):
        self.recent_date = timezone.now()
        self.save()

    def __str__(self):
        return self.category


class Stock(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    shares = models.CharField(max_length=50)
    cust_number = models.ForeignKey('portfolio.Customer')
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    recent_date = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def created(self):
        self.recent_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
