from django.shortcuts import render ,redirect
from .forms import RegisterForm
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
    return render(request,'login.html')

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(form.errors)
        if form.is_valid():
            print('the if case is working')
            print('username is the',form.cleaned_data['username'])

        else:
            form = RegisterForm()
            print('the else case is working')
    return render(request,'register.html')