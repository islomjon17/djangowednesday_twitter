from typing import Any
from django import forms

from .models import Meep, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Profile extract form

class ProfilePictureForm(forms.ModelForm):
    profile_image = forms.ImageField(label="Profile Picture")



    class Meta:
        model = Profile
        fields = ("profile_image", )
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
        exclude = ("user", "likes", )


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
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form text text muted"><small>Required, 150 characters or fewere. Letters, digits and @/./+/- only. </small>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form text text muted small"><li> Your password can\'t be too similar to your other personal information. </li><li>Your password is not save </li> </ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form text text muted small"> <small> Enter the same password as before, for verification </small> </span>'



