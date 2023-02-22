from django.urls import path,include
from .import views

app_name = 'seller_app'
urlpatterns = [
    path('seller_home',views.seller_home,name='seller_home'),
    path('addproduct',views.addproduct,name='addproduct')

]