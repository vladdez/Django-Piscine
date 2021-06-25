#!/bin/sh 
python3 -m venv django_venv
source django_venv/bin/activate

python3 -m pip3 install --upgrade pip
pip3 install -r requirement.txt
mkdir project
cp index.html project
cp settings.py project
cd project
pwd

django-admin startproject d04 .
python manage.py startapp ex00

mkdir ex00/templates
mkdir ex00/templates/ex00
cp index.html ex00/templates/ex00
cp settings.py d04
rm settings.py
rm index.html

echo "from django.shortcuts import render

def markdown(request):
   return render(request, 'ex00/index.html') " > ex00/views.py


echo "from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.markdown, name='markdown'), 
]
" > ex00/urls.py

echo "from django.conf.urls import url, include

urlpatterns = [
    url(r'^ex00/', include('ex00.urls')), 
]" > d04/urls.py



python manage.py migrate
python manage.py runserver
