from django.core.exceptions import MiddlewareNotUsed
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def login(request):
    # user = 'not logged in'

    return render(request, 'login.html')

def register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        print(password1)
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                print("Username Already Exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already Used')
                print("Email Already Used")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, first_name=first_name, last_name=last_name, email=email)
                user.save();
                print('success')
                return redirect('/')
        else:
            messages.info(request, 'Password is not matching...')
            print('Password is not matching...')
            return redirect('register')
    else:
        return render(request, 'register.html')
    
    