from django.urls import path
from . import views

urlpatterns = [
    path('',views.log,name='login'),
    path('registration',views.reg,name='registration'),
    path('home',views.hom,name='home'),


    path('login_btn',views.log_btn),
    path('register',views.register),
]