from django import forms

class LoginForm(forms.Form):
    username = forms.EmailField()
    password = forms.CharField()