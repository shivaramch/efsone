from django.utils import timezone
from .models import *
from django.shortcuts import render, get_object_or_404
# from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse


def home(request):
    return render(request, 'portfolio/home.html',
                  {'portfolio': home})


@login_required
def customer(request):
    customers = Customer.objects.filter(created_date__lte=timezone.now())
    # investments = Investment.objects.filter(acquired_date__lte=timezone.now())
    # stocks = Stock.objects.filter(recent_date__lte=timezone.now())
    return render(request, 'portfolio/customer.html',
                  {'customers': customers})
    # return render(request, 'customers/customer.html',
    #               {'customers': customers, 'investments': investments, 'stocks': stocks})


@login_required
def customer_edit(request, cust_number):
    customer = get_object_or_404(Customer, pk=cust_number)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        # form = CustomerForm(request.CUSTOMER, )
        if form.is_valid():
            customer = form.save(commit=False)
            customer.cust_number = request.user.pk
            customer.name = request.user
            customer.address = request.user
            customer.city = request.user
            customer.state = request.user
            customer.zipcode = request.user
            customer.email = request.user
            customer.cell_phone = request.user
            customer.updated_date = timezone.now()
            customer.save()
            return reverse('customers:customer_edit', request.user.pk)
    else:
        form = CustomerForm()
        return render(request, 'portfolio/customer_edit.html', {'form': form})


@login_required
def stock(request):
    stocks = Stock.objects.filter(recent_date__lte=timezone.now())
    return render(request, 'portfolio/stock.html', {'stocks': stocks})


@login_required
def investment(request):
    investments = Investment.objects.filter(acquired_date__lte=timezone.now())
    return render(request, 'portfolio/investment.html', {'investments': investments})
