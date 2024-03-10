
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.api, name="api"),
    path('api/', views.api, name="api" ),
    path('upload/', views.handle_files, name='handle_files'),
    path('download-excel/', views.download_excel, name='download_excel'),
    path('download-rap/', views.download_rap, name='download_rap'),
    

     
    
]