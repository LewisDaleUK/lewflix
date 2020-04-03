from django.shortcuts import render, get_object_or_404

from tvshows.models import TVShow, Season


def index(request):
    tvshows = TVShow.objects.all()
    return render(request, 'tvshows/index.html', {'tvshows': tvshows})


def get_tv_show(request, tv_show):
    tv_show = get_object_or_404(TVShow, pk=tv_show)
    seasons = Season.objects.filter(tv_show=tv_show)
    return render(request, 'tvshows/view_tv_show.html', {'tv_show': tv_show, 'seasons': seasons})


def get_season(request):
    pass


def get_episode(request):
    pass
