from django.shortcuts import render,redirect
from common.models import Customer
from seller.models import Product
from .models import Cart
from django.http import JsonResponse


# Create your views here.


def customer_home(request):
    customer_details = Customer.objects.get(id=request.session['customer'])
    cname = customer_details.name
    product_details = Product.objects.all()

    return render(request, 'customer_templates/customer_home.html', {'cname': cname, 'products': product_details})


def cus_profile(request):
    msg=''
    customer = Customer.objects.get(id = request.session['customer'])
    if request.method == 'POST':
        name= request.POST['name']
        phone =request.POST['phone']
        
        address= request.POST['address']
        customer= Customer.objects.filter(id = request.session['customer']).update(name=name,phone=phone,address=address)
        customer = Customer.objects.get(id = request.session['customer'])
        msg='success fully updated'
        return render(request, 'customer_templates/cus_profile.html',{'customer':customer,'msg':msg})
    return render(request, 'customer_templates/cus_profile.html',{'customer':customer})


def change_pswd(request):
    error = ''
    succsess = ''
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        customer_details = Customer.objects.get(id=request.session['customer'])

        if old_password == customer_details.password:
            if len(new_password) >= 8:
                if new_password == confirm_password:
                    customer_details.password=new_password
                    customer_details.save()
                    succsess='success'

                else:
                    error = 'password does not match'
            else:
                error = 'password should be minimum 8 charecter'

        else:
            error = 'check your old password'

    return render(request, 'customer_templates/change_pswd.html',{'succsess':succsess,'error':error})


def p_details(request,pid):
    msg = ''
    product_detail = Product.objects.get(id = pid)
    if request.method == 'POST':
        item = Cart.objects.filter(customer_id = request.session['customer'],product_id = pid).exists()

        if not item:

            cart_item = Cart(customer_id = request.session['customer'],product_id = pid)
            cart_item.save()
            return redirect('customer_app:cart')
        else:
            msg = 'item already in cart'

        

    return render (request,'customer_templates/p_details.html',{'product':product_detail,'message':msg})

def cart(request):
    items = Cart.objects.filter(customer = request.session['customer'])



    return render(request,'customer_templates/cart.html',{'items':items})

def total_price(request):
    qty = request.POST['qty']
    pid = request.POST['pid']

    product = Product.objects.filter(id = pid).values('price')
    
    total = int(qty)*product[0]['price']

    print(total)

    return JsonResponse({'total':total})


def edited_profile(request):
     

    return redirect('customer_app:cus_profile')
