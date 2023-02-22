from django.urls import path,include
from .import views

app_name = 'eco_admin_app'
urlpatterns = [
    path('home',views.home,name='home'),
    path('view_seller',views.view_seller,name='view_seller'),
    path('view_customer',views.view_customer,name='view_customer'),
    path('view_products',views.view_products,name='view_products'),
    path('approve_seller',views.approve_seller,name='approve_seller'),
    path('btn_approve_seller/<int:sid>',views.btn_approve_seller,name='btn_approve_seller'),
    path('btn_reject_seller/<int:sid>',views.btn_reject_seller,name='btn_reject_seller'),
   

]