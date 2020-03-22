from django.http import HttpResponse
from django.shortcuts import render

from movies.models import Movie


def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})
