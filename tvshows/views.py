from django.shortcuts import render, get_object_or_404

from tvshows.models import TVShow, Season, Episode


def index(request):
    tvshows = TVShow.objects.all()
    return render(request, 'tvshows/index.html', {'tvshows': tvshows})


def get_tv_show(request, tv_show):
    tv_show = get_object_or_404(TVShow, pk=tv_show)
    seasons = Season.objects.filter(tv_show=tv_show)
    return render(request, 'tvshows/view_tv_show.html', {'tv_show': tv_show, 'seasons': seasons})


def get_season(request, tv_show, season):
    tv_show = get_object_or_404(TVShow, pk=tv_show)
    tv_season = get_object_or_404(Season, tv_show=tv_show, number=season)
    episodes = Episode.objects.filter(season=tv_season)
    return render(request, 'tvshows/view_season.html', {'tv_show': tv_show, 'season': tv_season, 'episodes': episodes})


def get_episode(request, tv_show, season, episode):
    tv_show = get_object_or_404(TVShow, pk=tv_show)
    tv_season = get_object_or_404(Season, number=season)
    tv_episode = get_object_or_404(Episode, episode_number=episode, season=tv_season)

    next_episode = get_next_episode(tv_show, tv_season, tv_episode)

    return render(request, 'tvshows/view_episode.html', {
        'tv_show': tv_show,
        'season': tv_season,
        'episode': tv_episode,
        'next_episode': next_episode
    })


def get_next_episode(tv_show, season, current_episode):
    episode_list = Episode.objects.filter(season=season).order_by('episode_number')
    season_list = Season.objects.filter(tv_show=tv_show).order_by('number')

    if current_episode.episode_number < episode_list.last().episode_number:
        return episode_list.filter(episode_number=current_episode.episode_number + 1).first()

    if season.number < season_list.last().number:
        return Episode.objects.filter(season__number=season.number+1).order_by('episode_number').first()

    return None
