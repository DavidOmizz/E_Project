from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('thankyou', views.thankyou, name='thankyou'),
    path('product-detail/<int:pk>/', views.productDetail, name='product-detail')
]
