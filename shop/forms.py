from django import forms
from django.forms import ModelForm
from .models import *
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField


# class ContactForm(forms.Form):
#     name=forms.CharField(max_length=50)
#     email=forms.EmailField(max_length=50)
#     phone=forms.IntegerField()
#     desc=forms.CharField()

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields =['name','email','Address','city','state','Zipcode']
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields =['Payment']

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name','email','phone','desc']

class SubscriberForm(forms.ModelForm):
    class Meta:
        model=Subscribers
        fields=['subscribers']
        
class HelpForm(forms.ModelForm):
    class Meta:
        model=Help
        fields =['problem']

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields =['name','contact_no','address']