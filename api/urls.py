
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.api, name="api"),
    path('api/', views.api, name="api" ),
    path('upload/', views.handle_files, name='handle_files'),
    path('download-excel/', views.download_excel, name='download_excel'),
    path('download-rap/', views.download_rap, name='download_rap'),
    path('add_tab_aux/', views.add_tab_aux, name='add_tab_aux'),
    path('success', views.tab_aux_success, name='success_page'),
    path('tab_aux_list/', views.tab_aux_list, name='tab_aux_list'),
    path('tab_aux_delete/<int:pk>/', views.tab_aux_delete, name='tab_aux_delete'),
    path('tab_aux_edit/<int:pk>/', views.tab_aux_edit, name='tab_aux_edit'),
    path('index', views.index, name='index'),
    # Tables
    path('listAffilie', views.listAffilie, name='listAffilie'),
    path('listNts', views.listNts, name='listNts'),
    path('listBanque', views.listBanque, name='listBanque'),
    path('listCoffre', views.listCoffre, name='listCoffre'),
    # Pages 
    path('cbl', views.cbl, name='cbl'),
    path('banque', views.banque, name='banque'),
    path('coffre', views.coffre, name='coffre'),
    # add 
    path('addAffilie', views.addAffilie, name='addAffilie'),
    path('addNts', views.addAffilie, name='addNts'),
    path('addBanque', views.addBanque, name='addBanque'),
    path('addCoffre', views.addCoffre, name='addCoffre'),





]