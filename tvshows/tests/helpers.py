import datetime
from faker import Faker

from tvshows.models import TVShow, Season, Episode


def create_tv_show(title, year, image_url):
    start_year = datetime.date(year, 1, 1)
    return TVShow.objects.create(title=title, start_year=start_year, image_url=image_url)


def create_season(tv_show, number):
    return Season.objects.create(tv_show=tv_show, number=number)


def create_episode(title, episode_number, description, season):
    return Episode.objects.create(title=title, episode_number=episode_number, description=description, season=season)


def create_random_seasons(tv_show):
    fake = Faker()

    seasons = []
    for i in range(fake.random_int(min=1, max=4), fake.random_int(min=5, max=10)):
        seasons.append(create_season(tv_show, i))

    return seasons


def create_random_episodes(season):
    fake = Faker()

    episodes = []

    for i in range(fake.random_int(min=1, max=4), fake.random_int(min=5, max=20)):
        episodes.append(create_episode(fake.name(), i, fake.paragraph(), season))
    return episodes
