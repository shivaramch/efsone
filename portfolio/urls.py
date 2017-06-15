"""efs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^customer/$', views.customer, name='customer'),
    url(r'^customer/(?P<cust_number>\d+)/delete/$', views.customer_delete, name='customer_delete'),
    url(r'^customer/(?P<cust_number>\d+)/edit/$', views.customer_edit, name='customer_edit'),
    url(r'^customer/create/$', views.customer_new, name='customer_new'),
    url(r'^investment/$', views.investment, name='investment'),
    url(r'^investment/(?P<cust_number>\d+)/delete/$', views.investment_delete, name='investment_delete'),
    url(r'^investment/(?P<cust_number>\d+)/edit/$', views.investment_edit, name='investment_edit'),
    url(r'^investment/create/$', views.investment_new, name='investment_new'),
    url(r'^stock/$', views.stock, name='stock'),
    url(r'^stock/(?P<cust_number>\d+)/delete/$', views.stock_delete, name='stock_delete'),
    url(r'^stock/(?P<cust_number>\d+)/edit/$', views.stock_edit, name='stock_edit'),
    url(r'^stock/create/$', views.stock_new, name='stock_new'),

]
