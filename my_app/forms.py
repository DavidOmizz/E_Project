from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    customer_name = forms.CharField(label = 'Full Name', widget= forms.TextInput(attrs={'placeholder':'Enter full name', 'class': 'form-control', 'required':True}))
    customer_number = forms.CharField(label = 'Phone no.', widget= forms.NumberInput(attrs={'placeholder':'Enter your Phone number', 'class': 'form-control', 'minlength': 11, 'type': 'number', 'required':True}))
    customer_email = forms.EmailField(label = 'Email', widget= forms.TextInput(attrs={'placeholder':'Enter your email for poultry advice, insights and news letter', 'class': 'form-control', 'type': 'email'}))
    message = forms.CharField(label = 'Message', widget= forms.Textarea(attrs={'placeholder':'Send us messages about your order', 'class': 'form-control','required':True}))
    shipping_address = forms.CharField(label = 'Your location', widget = forms.TextInput(attrs={'placeholder':'Enter your your location', 'class': 'form-control','minlength':10, 'required':True}))
    quantity = forms.CharField(label = 'Product Quantity', widget= forms.NumberInput(attrs={'placeholder':'Enter the product quantity', 'class': 'form-control','required':True}))
    class Meta:
        model = Order
        fields = ('customer_name', 'customer_number','customer_email','quantity','message','shipping_address')