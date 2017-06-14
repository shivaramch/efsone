from django.contrib import admin
from .models import Customer, Investment, Stock

admin.site.register(Customer)
admin.site.register(Investment)
admin.site.register(Stock)
