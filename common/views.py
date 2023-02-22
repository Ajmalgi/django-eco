from django.shortcuts import render, redirect
from . models import Customer
from . models import Seller
from random import randint
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.decorators import api_view

import logging
# Create your views here.

logger = logging.getLogger('django')


def common_index(request):
    logger.info("this is info message")
    return render(request, 'common_templates/index.html')




def checkout(request):
    return render(request, 'common_templates/checkout.html')


def customer_reg(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        address = request.POST['address']
        phone = request.POST['phone']

        new_customer = Customer(name=username, email=email, password=password,address=address,phone=phone)
        new_customer.save()  # inserting in to table as row

    return render(request, 'common_templates/customer_reg.html')


def customer_login(request):
     msg = ''
     if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            customer = Customer.objects.get(email=email,password=password)
            request.session['customer'] = customer.id
            return redirect('customer_app:customer_home') #redirect (app_name:url name)
        except:
            msg ='Invalid credentials'
     return render(request,'common_templates/customer_login.html',{'message':msg})


def seller_login(request):
    msg=''
    if request.method == 'POST':
        seller_id = request.POST['seller_id']
        password = request.POST['password']
        try:
            seller = Seller.objects.get(user_name=seller_id,password=password)
            request.session['seller'] = seller.id
            return redirect('seller_app:seller_home') #redirect (app_name:url name)
        except:
            msg ='Invalid credentials'
    
    return render(request, 'common_templates/seller_login.html',{'message':msg})


def seller_reg(request):
    msg = ''
    if request.method == 'POST':

            seller_name = request.POST['seller_name']
            email = request.POST['email']
            phone = request.POST['phone']
            account = request.POST['account']
            ifsc = request.POST['ifsc']
            seller_pic = request.FILES['seller_pic']
            address = request.POST['address']
            user_name= randint(1111, 9999)
            pwd = 'sell-'+str(user_name)+'-'+phone[6:10]

            newseller = Seller(name=seller_name, email=email, phone=phone, account=account,ifsc=ifsc,
             seller_pic=seller_pic, address=address, user_name=user_name,password=pwd)
            newseller.save()
            msg = 'created successfully'
            email_subject='account user name and password'
            email_content='user name :'+str(user_name) + 'password' + pwd

            # send_mail(
            #     email_subject,
            #     email_content,
            #     settings.EMAIL_HOST_USER,
            #     [email,]
            # )
    return render(request, 'common_templates/seller_reg.html',{'message':msg})

@api_view(['GET'])
def index(request):
    return Response('congratulations, you have created')

@api_view(['GET'])
def float(request):
    return Response(4)

