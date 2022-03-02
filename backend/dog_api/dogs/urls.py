from django.urls import path
from . import views
from django.urls import include, re_path

urlpatterns = [
    re_path(r'^dog-list/$', 
        views.ListDogs.as_view(), 
        name=views.ListDogs.name),


    re_path(r'^dog-list/(?P<pk>[0-9]+)/$', 
        views.DetailDog.as_view(),
        name=views.DetailDog.name),

    re_path(r'^breed-list/$', 
        views.ListBreeds.as_view(), 
        name=views.ListBreeds.name),


    re_path(r'^breed-list/(?P<pk>[0-9]+)/$', 
        views.DetailBreed.as_view(),
        name=views.DetailBreed.name),

    
]