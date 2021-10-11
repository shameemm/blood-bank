from django.urls import path

from . import views
from accounts.views import login
urlpatterns = [
    
    path('', login ),
    path('register', views.register, name='register')
    
    
]