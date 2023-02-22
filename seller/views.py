from django.shortcuts import render
from common.models import Seller
from . models import Product

# Create your views here.

def seller_home(request):
    seller_details = Seller.objects.get(id=request.session['seller'])
    sname = seller_details.name
    product_details = Product.objects.filter(seller_id = request.session['seller'])

    return render(request,'seller_templates/seller_home.html',{'sname':sname,'products':product_details})

def addproduct(request):
     
    if request.method == 'POST':
        product_name = request.POST['product_name']
        category = request.POST['category']
        product_no = request.POST['product_no']
        product_des = request.POST['product_des']
        price = request.POST['price']
        stock = request.POST['stock']
        image = request.FILES['image']
        seller=request.session['seller']

        new_product= Product(product_name=product_name,category=category,product_no=product_no,product_des=product_des,price=price,stock=stock,image=image,seller_id=seller)
        new_product.save()  
    return render(request,'seller_templates/addproduct.html')