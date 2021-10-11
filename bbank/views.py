from django.core.exceptions import MiddlewareNotUsed
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import JsonResponse
from .models import Details
# Create your views here.
def display(request):
    user = request.session.get('user_username')
    if user is not None:
                print(user)
                det_list = Details.objects.all()
                return render(request, 'display.html', {"details" : det_list});
    else:
                return render(request, 'login.html')

# def logout(request):
#     del request.session['user_username']
    
    
#     return redirect('/')
           