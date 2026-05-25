from django.urls import path
from . import views

urlpatterns = [
    path('',              views.index,      name='index'),
    path('catalog/',      views.catalog,    name='catalog'),
    path('catalog/<int:pk>/', views.car_detail, name='car_detail'),
    path('tradein/',      views.tradein,    name='tradein'),
    path('credit/',       views.credit,     name='credit'),
    path('about/',        views.about,      name='about'),
    path('contacts/',     views.contacts,   name='contacts'),
]