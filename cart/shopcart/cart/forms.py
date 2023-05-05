from django import forms

from .models import *

       
class UserRegistrationForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = userregistration
        fields = ('Name', 'Mobile', 'Email', 'Password', 'Address', 'State', 'Country')


class loginform(forms.ModelForm):
    class Meta:
        model = login
        fields = ('Email','Password')
        widgets = {
             'Email' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
             'Password' : forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
        }
        
        
        
        
class groceryform(forms.ModelForm):
    class Meta:
        model = Grocery
        fields = ('product','amount','image')
        widgets = {
             'product' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Item','id':'productid'}),
             'amount' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity','id':'amountid'}),
             'image':forms.FileInput(attrs={ 'id':'imageid'}) 

        }