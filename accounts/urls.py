from django.urls import path

from . import views
from accounts.views import login
from bbank.views import display
urlpatterns = [
    
    path('', login ),
    path('register', views.register, name='register'),
    path('display', display, name='display'),
    path('logout', views.logout, name='logout')
    
    
]