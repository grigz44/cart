from django.urls import path
from . import views
from .views import*




urlpatterns = [
    
    
    
path('register/', views.register, name='register'),
path('login/', views.u_login, name='login'),
path('adm/addGrocery/', views.home_Grocery, name='add-Grocery'),
path('deleteex/', views.delete_data_Grocery, name='deleteex'),
path('editcourse/<id>', views.editcourse, name='editcourse'),
path('', views.index, name='index'),
path('product/<int:pk>/', views.product_detail, name='product_detail'),
path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
path('cart/', views.cart, name='cart'),
path('update_cart/', views.update_cart, name='update_cart'),
path('delete_from_cart/', views.delete_from_cart, name='delete_from_cart'),
]