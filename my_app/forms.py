from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    # customer_name = forms.CharField(label = 'name', widget= forms.TextInput(attrs={'placeholder':'Enter full name', 'class': 'form-control', 'required':True}))
    # customer_number = forms.CharField(label = 'number', widget= forms.NumberInput(attrs={'placeholder':'Enter your number', 'class': 'form-control', 'minlength': 11, 'type': 'number', 'required':True}))
    # customer_email = forms.EmailField(label = 'email', widget= forms.TextInput(attrs={'placeholder':'Enter your mail', 'class': 'form-control', 'type': 'email'}))
    # message = forms.CharField(label = 'content', widget= forms.Textarea(attrs={'placeholder':'Message', 'class': 'form-control','required':True}))
    # shipping_address = forms.CharField(label = 'shipping_address', widget = forms.TextInput(attrs={'placeholder':'Shipping Address', 'class': 'form-control','minlength':10, 'required':True}))
    # quantity = forms.CharField(label = 'quantity', widget= forms.NumberInput(attrs={'placeholder':'Enter the quantity', 'class': 'form-control','required':True}))
    class Meta:
        model = Order
        fields = ('customer_name', 'customer_number','customer_email','quantity','message','shipping_address')