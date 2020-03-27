from datetime import datetime
from django.test import TestCase
from faker import Faker

from tvshows.models import Episode, Season, TVShow


def create_season(number):
    tv_show = TVShow.objects.create(title="Test TV Show", start_year=datetime.now(), image_url="http://fake-url")
    return Season.objects.create(number=number, tv_show=tv_show)


def create_random_episodes(season, length):
    fake = Faker()

    episodes = []
    for i in range(0, length):
        episodes.append(
            Episode.objects.create(title=fake.job(), episode_number=i, description=fake.paragraph(), season=season)
        )

    return episodes


class TestSeason(TestCase):
    def test_can_create_season(self):
        created_season = create_season(4)
        retrieved_season = Season.objects.get(id=created_season.id)

        self.assertEqual(created_season, retrieved_season)

    def test_convert_season_to_string(self):
        created_season = create_season(4)

        self.assertEqual("04", str(created_season))

    def test_season_can_get_list_of_episodes(self):
        season = create_season(4)
        created_episodes = create_random_episodes(season, 10)

        retrieved_episodes = list(Episode.objects.filter(season_id=season.id))

        self.assertEqual(created_episodes, retrieved_episodes)
