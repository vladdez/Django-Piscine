from django.urls import path
from . import views

urlpatterns = [
#    path('', views.index),
    path('registration/', views.registration),
    path('login/', views.login),
    path('logout/', views.logout),
    path('profile/', views.profile),
]
