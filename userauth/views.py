from django.shortcuts import render ,redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


def index(request):
    return render(request,'index.html')


def kozhikkod(request):
    return redirect('https://en.wikipedia.org/wiki/Kozhikode')

def malapuram(request):
    return redirect('https://en.wikipedia.org/wiki/Malappuram')

def kannur(request):
    return redirect('https://en.wikipedia.org/wiki/Kannur')

def kochi(request):
    return redirect('https://en.wikipedia.org/wiki/Kochi')

def palakkad(request):
    return redirect('https://en.wikipedia.org/wiki/Palakkad')


def user_login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            print('the if case is working')
            pass
        else:
            print('the else case is working')
            messages.error(request, 'please enter the valid')
            return redirect('userauth:user_login')
    context = {
        "form":form
    }
    return render(request,'login.html',context)

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)  
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email = email).exists():
                messages.error(request, 'The email is already taken please take another eamil')
                return redirect('userauth:user_register')
            print(email)
            form.save() 
        else:
            print(form.errors)
    else:
        form = RegisterForm()
        print('this  calling')
    context = {
        'form': form
    }
    return render(request, 'register.html', context)
