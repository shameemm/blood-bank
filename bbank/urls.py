from django.urls import path

from . import views
from accounts.views import login, register,logout
urlpatterns = [
    
    path('', login ),
    path('register',register),
    path('display', views.display, name='display'),
    path('logout', logout, name='logout'),
    path('add_donor', views.add_donor, name='add_donor')
    
]