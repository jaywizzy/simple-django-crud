from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

# Create your views here.

def products_list(request):
	products = Product.objects.all()
	return render(request, 'products.html', {'products': products})

def create_product(request):
	if request.method == 'POST':
		form = ProductForm(request.POST or None)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = ProductForm()
	return render(request, 'products_form.html', {'form': form})

def edit_product(request, id):
	product = Product.objects.get(id=id)
	form = ProductForm(request.POST or None, instance=product)
	if form.is_valid():
		form.save()
		return redirect('products_list')

	return render(request, 'products_form.html', {'form': form, 'product': product})

def delete_product(request, id):
	product = Product.objects.get(id=id)
	if request.method == 'POST':
		product.delete()
		return redirect('products_list')
	return render(request, 'delete_product.html', {'product': product})

	
