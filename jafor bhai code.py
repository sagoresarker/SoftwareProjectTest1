#urls my app

from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name = 'home')
]

#views myapp

from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello World")


#urls mysite

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls'))
]
