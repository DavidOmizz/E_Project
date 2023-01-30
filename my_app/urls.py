from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('product-detail/<int:pk>/', views.productDetail, name='product-detail'),
    path('/<slug:category_slug>/', views.index, name='category_slug')
    # path('thankyou', views.thankyou, name='thankyou'),
]
