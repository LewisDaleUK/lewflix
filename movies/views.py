from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from movies.models import Movie


def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})


def get_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)
    return render(request, 'movies/movie_view.html', {'movie': movie})

