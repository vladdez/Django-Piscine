#!/bin/bash -i
python3 -m venv django_venv
source django_venv/bin/activate

python3 -m pip3 install --upgrade pip
pip3 install -r requirement.txt

mkdir hello_world
cd hello_world
django-admin startproject config .
python manage.py startapp pages

echo "from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('Hello, World!')"  > pages/views.py


echo "from django.urls import path
from .views import homePageView

urlpatterns = [
    path('', homePageView, name='home')
]" > pages/urls.py

echo "from django.contrib import admin
from django.urls import path, include # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/', include('pages.urls')), # new
]" > config/urls.py
python manage.py migrate
python manage.py runserver

