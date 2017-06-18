from django.utils import timezone
from .models import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.core.urlresolvers import reverse, reverse_lazy


def home(request):
    return render(request, 'portfolio/home.html',
                  {'portfolio': home})


@login_required
def customer(request):
    customer = Customer.objects.filter(created_date__lte=timezone.now())
    return render(request, 'portfolio/customer.html',
                  {'customers': customer})


# @login_required
# def customer_new(request):
#     if request.method == "POST":
#         form = CustomerForm(request.POST)
#         if form.is_valid():
#             customer = form.save(commit=False)
#             customer.cust_number = request.user.pk
#             customer.created_date = timezone.now()
#             customer.save()
#             return redirect('portfolio:customer', request.customer.pk)
#     else:
#         form = CustomerForm()
#     return render(request, 'portfolio/customer_new.html', {'form': form})


@login_required
def customer_edit(request, cust_number):
    customer = get_object_or_404(Customer, pk=cust_number)
    if request.method == "POST":
        # update
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.cust_number = cust_number
            customer.updated_date = timezone.now()
            customer.save()
            customers = Customer.objects.filter(created_date__lte=timezone.now())
            return render(request, 'portfolio/customer.html',
                          {'customers': customer})
            # return redirect('portfolio/customer.html', request.customer.pk)
    else:
        # edit
        form = CustomerForm(instance=customer)
    return render(request, 'portfolio/customer_edit.html', {'form': form})


@login_required
def customer_delete(request, cust_number):
    customer = get_object_or_404(Customer, pk=cust_number)
    customer.delete()
    return redirect('portfolio:customer')


@login_required
def stock(request):
    stock = Stock.objects.filter(recent_date__lte=timezone.now())
    return render(request, 'portfolio/stock.html', {'stocks': stock})


@login_required
def stock_new(request):
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            customer.cust_number = request.user.pk
            stock.created_date = timezone.now()
            stock.save()
            return redirect('portfolio:stock', pk=request.stock.pk)
    else:
        form = StockForm()
    return render(request, 'portfolio/stock_new.html', {'form': form})


@login_required
def stock_edit(request, cust_number):
    print(cust_number)
    stock = get_object_or_404(Customer, pk=cust_number)
    if request.method == "POST":
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            stock = form.save(commit=False)
            customer.cust_number = request.user.pk
            stock.updated_date = timezone.now()
            stock.save()
            return redirect('portfolio:stock_edit', pk=request.stock.pk)
    else:
        form = StockForm(instance=stock)
    return render(request, 'portfolio/stock_edit.html', {'form': form})


@login_required
def stock_delete(request, cust_number):
    stock = get_object_or_404(Stock, pk=cust_number)
    stock.delete()
    return redirect('portfolio:stock')


@login_required
def investment(request):
    investment = Investment.objects.filter(acquired_date__lte=timezone.now())
    return render(request, 'portfolio/investment.html', {'investments': investment})


@login_required
def investment_new(request):
    # investment = get_object_or_404(customer.cust_number)
    if request.method == "POST":
        form = InvestmentForm(request.POST)
        if form.is_valid():
            investment = form.save()
            # investment.customer = investment.cust_number
            investment.created_date = timezone.now()
            investment.save()
            investment = Investment.objects.filter(acquired_date__lte=timezone.now())
            return render(request, 'portfolio/investment.html', {'investments': investment})
    else:
        form = InvestmentForm()
    return render(request, 'portfolio/investment_new.html', {'form': form})


@login_required
def investment_edit(request, cust_number):
    print(cust_number)
    investment = get_object_or_404(Customer, pk=cust_number)
    if request.method == "POST":
        print("if")
        form = InvestmentForm(request.POST, instance=investment)
        if form.is_valid():
            investment = form.save(commit=False)
            investment.cust_number = cust_number
            investment.updated_date = timezone.now()
            investment.save()
            return redirect('portfolio:investment_edit', pk=request.investment.pk)
    else:
        print("else")
        form = InvestmentForm(instance=investment)
    return render(request, 'portfolio/investment_edit.html', {'form': form})


@login_required
def investment_delete(request, cust_number):
    investment = get_object_or_404(Investment, pk=cust_number)
    investment.delete()
    return redirect('portfolio:investment')
