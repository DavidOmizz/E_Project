from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import OrderForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

def thankyou(request):
    return render(request, 'thankyou.html')

def index(request,category_slug=None):
    template_name = 'shop.html'
    product = Product.objects.all().order_by('-created_at')
    categories = None
    category = Category.objects.all()
    if category_slug:
        categories = get_object_or_404(Category,slug=category_slug)
        product = product.filter(categories=categories)
    return render(request, template_name, {'product': product, 'category':category, 'categories':categories} )


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