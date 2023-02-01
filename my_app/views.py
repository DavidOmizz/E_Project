from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

def thankyou(request):
    return render(request, 'thankyou.html')

def index(request):
    template_name = 'shop.html'
    product = Product.objects.all().order_by('-created_at')
    category = Category.objects.all()
    categoryID = request.GET.get('category')
    if categoryID:
        product = Product.objects.filter(category=categoryID)
    else:
        product = Product.objects.all().order_by('-created_at')
        
    return render(request, template_name, {'product': product, 'category':category} )

def category(request, pk):
    template_name = 'categories.html'
    category = Category.objects.get(id=pk)
    product = Product.objects.filter(category=category)

    return render(request, template_name, {'product':product})

def productDetail(request, pk):
    template_name = 'shop-single.html'
    checkout = 'thankyou.html'
    product = Product.objects.get(id=pk)
    custormer_order = None
    if request.method =='POST':
        orders = OrderForm(data=request.POST)
        if orders.is_valid():
             # Create Comment object but don't save to database yet
            custormer_order = orders.save(commit=False)
            # Assign the current post to the comment
            custormer_order.post = product
            # Save the comment to the database
            custormer_order.save()
            messages.success(request,'Order Placed succesffully')
            return render(request, checkout)
    else:
        orders = OrderForm()
    return render(request, template_name, {"product":product, 'orders':orders,'custormer_order':custormer_order})