from django import forms       

class RegisterForm(forms.Form):
    username = forms.CharField(label='username',max_length=50)
    email = forms.CharField(label='email',max_length=100)
    password = forms.IntegerField(label='password')
    conform_password = forms.IntegerField(label='conform_password')