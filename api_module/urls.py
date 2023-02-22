from django.urls import path
from . import views




urlpatterns = [
    path('add_student',views.add_student,name='add_student'),
    path('load_student',views.view_student,name='view_student'),
    path('delete_student/<int:sid>',views.delete_student,name='delete_student'),
    path('update_student/<int:sid>',views.update_student,name='update_student'),

]