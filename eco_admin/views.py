from django.shortcuts import render,redirect
from common.models import Seller
from common.models import Customer
from seller.models import Product

# Create your views here.

def home(request):
    return render(request,'ecoadmin/home.html')

def view_seller(request):
    seller = Seller.objects.all()


    return render(request,'ecoadmin/view seller.html',{'seller':seller})

def view_customer(request):
    customer = Customer.objects.all()
    return render(request,'ecoadmin/view customer.html',{'customer':customer})

def view_products(request):
    product = Product.objects.all()
    return render(request,'ecoadmin/view products.html',{'product':product})

def approve_seller(request):
    seller = Seller.objects.filter(status = 'pending')
    return render(request,'ecoadmin/approve seller.html',{'seller':seller})

def btn_approve_seller(request,sid):

    seller = Seller.objects.filter(id = sid).update(status='approved')
    return redirect('eco_admin_app:approve_seller')


def btn_reject_seller(request,sid):

    seller = Seller.objects.filter(id = sid).update(status='rejected')
    return redirect('eco_admin_app:approve_seller')


