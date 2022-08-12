from django.urls import re_path as url
from . import views

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^peliculas/$', views.PeliculaListView.as_view(), name='peliculas'),
    url(r'^pelicula/(?P<pk>\d+)$', views.PeliculaDetailView.as_view(), name='pelicula-detail')
     
]