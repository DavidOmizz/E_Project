from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q


# Create your views here.

def thankyou(request):
    return render(request, 'thankyou.html')

# def index(request):
#     template_name = 'shop.html'
#     product = Product.objects.all().order_by('-created_at')
#     category = Category.objects.all()
#     categoryID = request.GET.get('category')
#     if categoryID:
#         product = Product.objects.filter(category=categoryID)
#     else:
#         product = Product.objects.all().order_by('-created_at')

#     query = request.GET.get('q')
#     if query:
#         product = Product.objects.filter(Q(product_name__icontains = query) | Q(category__icontains= query)).order_by('-created_at')
#         return product
#     else:
#         product = Product.objects.all()
#     return render(request, template_name, {'product': product, 'category':category} )

def index(request):
    template_name = 'shop.html'
    product = Product.objects.all().order_by('-created_at')
    category = Category.objects.all()
    categoryID = request.GET.get('category')
    query = request.GET.get('q')
    message = ''
    category_id = request.GET.get('category')

#     if categoryID and query:
#         product = Product.objects.filter(
#             Q(category=categoryID) & 
#             (Q(product_name__icontains=query) | 
#              Q(category__icontains=query))
#         ).order_by('-created_at')
#     elif categoryID:
#         product = Product.objects.filter(category=categoryID).order_by('-created_at')
#     elif query:
#         product = Product.objects.filter(
#             Q(product_name__icontains=query) | 
#             Q(category__icontains=query)
#         ).order_by('-created_at')

    if query or category_id:
        if query and category_id:
            product = product.filter(Q(product_name__icontains=query) & Q(category__id=categoryID))
        elif query:
            product = product.filter(product_name__icontains=query)
        else:
            product = product.filter(category__id=categoryID)

    if not product:
        message = 'No products found with the selected category'

    return render(request, template_name, {'product': product, 'category':category,'message': message})

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