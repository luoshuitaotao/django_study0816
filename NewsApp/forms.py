from django import forms
from .models import RegistrationData

class RegestrationForm(forms.Form):
    username = forms.CharField(max_length=100,
                               widget=forms.TextInput(attrs={
                                        'class':'form-control',
                                        'placeholder': 'Username',
    }))
    password = forms.CharField(max_length=100,
                               widget=forms.PasswordInput(attrs={
                                        'class':'form-control',
                                        'placeholder': 'Password',
    }))

    email = forms.CharField(max_length=100,
                               widget=forms.PasswordInput(attrs={
                                        'class':'form-control',
                                        'placeholder': 'Email',
    }))

    phone = forms.CharField(max_length=100,
                            widget=forms.PasswordInput (attrs={
                                'class': 'form-control',
                                'placeholder': 'Phone',
                            }))


class RegistrationModel(forms.ModelForm):
    class Meta:
        model = RegistrationData
        fields = [
            'username',
            'password',
            'email',
            'phone'
        ]

