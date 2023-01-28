from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    customer_name = forms.CharField(label = 'Full Name', widget= forms.TextInput(attrs={'placeholder':'Enter full name', 'class': 'form-control', 'required':True}))
    customer_number = forms.CharField(label = 'Mobile no.', widget= forms.NumberInput(attrs={'placeholder':'Enter your mobile number', 'class': 'form-control', 'minlength': 11, 'type': 'number', 'required':True}))
    customer_email = forms.EmailField(label = 'Email', widget= forms.TextInput(attrs={'placeholder':'Enter your mail', 'class': 'form-control', 'type': 'email'}))
    message = forms.CharField(label = 'Message', widget= forms.Textarea(attrs={'placeholder':'Send us messages about your order', 'class': 'form-control','required':True}))
    shipping_address = forms.CharField(label = 'Shipping Address', widget = forms.TextInput(attrs={'placeholder':'Enter your shipping address', 'class': 'form-control','minlength':10, 'required':True}))
    quantity = forms.CharField(label = 'Quantity', widget= forms.NumberInput(attrs={'placeholder':'Enter the quantity', 'class': 'form-control','required':True}))
    class Meta:
        model = Order
        fields = ('customer_name', 'customer_number','customer_email','quantity','message','shipping_address')