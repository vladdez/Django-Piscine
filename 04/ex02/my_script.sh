#!/bin/sh 
python3 -m venv django_venv
source django_venv/bin/activate

python3 -m pip3 install --upgrade pip
pip3 install -r requirement.txt
mkdir project
cp ex02.html project
cp settings.py project
cd project

django-admin startproject d04 .
python manage.py startapp ex02

mkdir ex02/templates
mkdir ex02/templates/ex02

cp ex02.html ex02/templates/ex02
cp settings.py d04

rm settings.py
rm ex02.html 

echo "from django.shortcuts import render
from .forms import MyForm
import logging

logger = logging.getLogger(__name__)
def ex02(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            logger.debug(form.cleaned_data['subject'])
    else:
        form = MyForm()
    try:
        with open('ex02/debug.log', 'r') as file:
            cont = file.readlines()
    except:
        cont = ''
        print('Wrong file ')
    return render(request, 'ex02/ex02.html', {'form':form, 'cont':cont}) 
   
   " > ex02/views.py


echo "from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.ex02, name='ex02'), 
]
    " > ex02/urls.py

echo "from django.conf.urls import url, include

urlpatterns = [
    url(r'^ex02/', include('ex02.urls')), 
]
    " > d04/urls.py

echo "from django import forms

class MyForm(forms.Form):
    subject = forms.CharField(label='subject', max_length=1000)
    " > ex02/forms.py



python manage.py migrate
python manage.py runserver
