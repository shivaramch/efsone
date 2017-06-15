from django import forms
from .models import Customer, Investment, Stock


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone',)


class InvestmentForm(forms.ModelForm):
    class Meta:
        model = Investment
        fields = ('category', 'description', 'acquired_value', 'acquired_date', 'recent_value', 'recent_date',)


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ('symbol', 'name', 'shares', 'purchase_price', 'recent_date',)
