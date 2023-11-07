
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include('firstapp.urls')),
    path('', include('react_app.url')),

]
