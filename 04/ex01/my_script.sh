#!/bin/sh 
python3 -m venv django_venv
source django_venv/bin/activate

python3 -m pip3 install --upgrade pip
pip3 install -r requirement.txt
mkdir project
cp base.html project
cp display.html project
cp django.html project
cp nav.html project
cp templates.html project
cp style1.css project
cp style2.css project
cp settings.py project
cd project
pwd

django-admin startproject d04 .
python manage.py startapp ex01

mkdir ex01/templates
mkdir ex01/templates/ex01
mkdir ex01/static
mkdir ex01/static/css
cp base.html ex01/templates/ex01
cp display.html ex01/templates/ex01
cp django.html ex01/templates/ex01
cp templates.html ex01/templates/ex01
cp nav.html ex01/templates/ex01
cp style1.css ex01/static/css
cp style2.css ex01/static/css
cp settings.py d04

rm settings.py
rm base.html 
rm display.html 
rm django.html 
rm templates.html 
rm nav.html 
rm style1.css 
rm style2.css 

echo "from django.shortcuts import render

def my_django(request):
   return render(request, 'ex01/django.html') 

def my_display(request):
   return render(request, 'ex01/display.html') 

def my_templates(request):
   return render(request, 'ex01/templates.html') 
   
   " > ex01/views.py


echo "from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^django/', views.my_django, name='my_django'), 
    url(r'^display/', views.my_display, name='my_display'), 
    url(r'^templates/', views.my_templates, name='my_templates'), 
]
    " > ex01/urls.py

echo "from django.conf.urls import url, include

urlpatterns = [
    url(r'^ex01/', include('ex01.urls')), 
]
    " > d04/urls.py



python manage.py migrate
python manage.py runserver
