from django import forms

from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone',)
        # values = ('customer.name', 'customer.city',)

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('author', 'text',)
