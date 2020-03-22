from django.http import HttpResponse

from movies.models import Movie


def index(request):
    movies = Movie.objects.all()

    if len(movies):
        response = ""
        for movie in movies:
            response += "{} <br />".format(movie)
        return HttpResponse(response)

    return HttpResponse("There are no movies currently available")
