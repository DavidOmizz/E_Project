from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('product-detail/<int:pk>/', views.productDetail, name='product-detail'),
    path('categories/<int:pk>/', views.category, name='categorys'),
    # path('thankyou', views.thankyou, name='thankyou'),
]
