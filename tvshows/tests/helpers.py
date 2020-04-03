import datetime
from faker import Faker

from tvshows.models import TVShow, Season


def create_tv_show(title, year, image_url):
    start_year = datetime.date(year, 1, 1)
    return TVShow.objects.create(title=title, start_year=start_year, image_url=image_url)


def create_random_seasons(tv_show):
    fake = Faker()

    seasons = []
    for i in range(fake.random_int(min=1, max=4), fake.random_int(min=5, max=10)):
        seasons.append(Season.objects.create(tv_show=tv_show, number=i))

    return seasons
