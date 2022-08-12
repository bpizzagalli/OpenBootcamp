from django.shortcuts import render
from .models import *
from django.views import generic
# Create your views here.



def index(request):
    num_directors=Director.objects.all().count()
    num_genre=Genre.objects.all().count()
    num_pelicula=Pelicula.objects.all().count()

    return render(
        request,
        'index.html',
        context={
            'num_directors': num_directors,
            'num_genre': num_genre,
            'num_pelicula': num_pelicula
        })


class PeliculaListView(generic.ListView):
    model = Pelicula
    context_object_name = 'my_pelicula_list'
    template_name = 'peliculas/my_arbitrary_template_name_list.html'

    def get_queryset(self):
        return Pelicula.objects.all()


class PeliculaDetailView(generic.DetailView):
    model = Pelicula