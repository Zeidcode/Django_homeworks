from django.shortcuts import render, redirect
from .models import Client, Product, Order
from django.utils import timezone
from datetime import timedelta
from .models import Order, Product
from .forms import ProductForm

def index(request):
    return render(request, 'index.html')

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': clients})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders.html', {'orders': orders})

def ordered_products(request):
    # Определяем временные интервалы для последних 7, 30 и 365 дней
    intervals = {
        'week': timezone.now() - timedelta(days=7),
        'month': timezone.now() - timedelta(days=30),
        'year': timezone.now() - timedelta(days=365)
    }
    
    # Получаем заказанные товары за каждый из интервалов
    ordered_products = {}
    for interval, start_date in intervals.items():
        orders = Order.objects.filter(order_date__gte=start_date)
        products = Product.objects.filter(order__in=orders).distinct()
        ordered_products[interval] = products

    return render(request, 'ordered_products.html', {'ordered_products': ordered_products})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_create.html', {'form': form})

def product_update(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_update.html', {'form': form})