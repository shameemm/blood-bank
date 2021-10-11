from django.urls import path

from . import views
from accounts.views import login
urlpatterns = [
    
    path('', views.login )
    
    
    
]