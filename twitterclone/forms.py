from django import forms

from .models import Meep
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User


class MeepForm(forms.ModelForm):
    body = forms.CharField(
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder":"Enter Your Kebaber Meep!",
                "class": "form-control"
                }
        ),
    label="",
    )
    
    class Meta:
        model = Meep
        exclude = ("user", )


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control',
'placeholder':'Email Address'
        }))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control',
'placeholder':'First name'
        }))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control',
'placeholder':'Last name'
        }))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


