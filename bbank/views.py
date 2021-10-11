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

def add_donor(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        place = request.POST['place']
        phone = request.POST['phone']
        bgrp = request.POST['bgrp']
        donor = Details.objects.create(name=name, age=age, place=place, phone=phone, bgrp=bgrp)
        donor.save()

        return redirect('display')
    else:
        user = request.session.get('user_username')
        if user is not None:
            print(user)
            
            return render(request, 'add_donor.html');
        else:
            return render(request, 'login.html')
           