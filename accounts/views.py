from django.core.exceptions import MiddlewareNotUsed
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def login(request):
    user = 'not logged in'
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        
        
        us = User.get_username
        
        if user is not None:
            
            # return redirect('display')
            print(dir(request.session))
            request.session['user_id'] = user.id
            request.session['user_username'] = user.username
            user = request.session.get('session_key')
           
            
            
            return JsonResponse(
                {'success': True},
                safe=False
            )
        else:
            messages.info(request, "Invalid Credentials")
            # return redirect('')
            return JsonResponse(
                {'success': False},
                safe=False
            )
    else:
        
        user = request.session.get('user_username')
        print(user)
       
        if user is not None:
            print(user)
            
            return redirect('display')
        else:
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

def logout(request):
    # del request.session['user_username']
    request.session.flush()
    
    
    return redirect('/')
    
    