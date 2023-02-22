from django.urls import path
from . import views

app_name = 'common_app'
urlpatterns = [
   path('',views.common_index,name='index'),
   path('checkout',views.checkout,name='checkout'),
   path('customer_reg',views.customer_reg,name='customer_reg'),
   path('customer_login',views.customer_login,name='customer_login'),
   path('seller_login',views.seller_login,name='seller_login'),
   path('seller_reg',views.seller_reg,name='seller_reg'),
   path('index',views.index,name='test_index'),
   path('float',views.float,name='float'),
   

]

