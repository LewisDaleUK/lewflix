from datetime import datetime
from django.test import TestCase

from tvshows.models import Season, TVShow


def create_tv_show(title, year):
    date_year = datetime.strptime(year, "%Y")
    return TVShow.objects.create(title=title, start_year=date_year, image_url="http://fake-url")


def create_random_season(tv_show, length):
    seasons = []

    for i in range(0, length):
        seasons.append(Season.objects.create(number=i, tv_show=tv_show))

    return seasons


class TestTVShow(TestCase):
    def test_can_create_tv_show(self):
        created_tv_show = create_tv_show("Test Title", "2020")
        retrieved_tv_show = TVShow.objects.get(id=created_tv_show.id)

        self.assertEqual(created_tv_show, retrieved_tv_show)

    def test_convert_season_to_string(self):
        tv_show = create_tv_show("Test Title", "2020")

        self.assertEqual("Test Title (2020)", str(tv_show))

    def test_season_can_get_list_of_episodes(self):
        tv_show = create_tv_show("Test Title", "2020")
        created_seasons = create_random_season(tv_show, 20)

        retrieved_seasons = list(Season.objects.filter(tv_show_id=tv_show.id))

        self.assertEqual(created_seasons, retrieved_seasons)
