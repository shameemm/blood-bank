from django.urls import path

from . import views
from accounts.views import login, register
urlpatterns = [
    
    path('', login ),
    path('register',register)
    
    
]