from django.urls import path,include
from . import views

app_name = 'customer_app'


urlpatterns = [
    path('customer_home',views.customer_home,name='customer_home'),
    path('cus_profile',views.cus_profile,name='cus_profile'),
    path('change_pswd',views.change_pswd,name='change_pswd'),
    path('p_details/<int:pid>',views.p_details,name='p_details'),
    path('cart',views.cart,name='cart'),
    path('total_price',views.total_price,name='total_price'),
    path('edited_profile',views.edited_profile,name='edited_profile'),

   

]