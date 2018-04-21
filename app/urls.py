from django.urls import path
from .views import *

urlpatterns = [
	path('', products_list, name='products_list'),
	path('create', create_product, name='create_product'),
	path('edit/<int:id>/', edit_product, name='update_product'),
	path('delete/<int:id>/', delete_product, name='delete_product'),
	
]