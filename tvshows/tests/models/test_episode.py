from datetime import datetime
from django.test import TestCase

from tvshows.models import Episode, Season, TVShow


def create_episode(title):
    tv_show = TVShow.objects.create(title="Test TV Show", start_year=datetime.now(), image_url="http://fake-url")
    season = Season.objects.create(number=1, tv_show=tv_show)
    episode = Episode.objects.create(title=title, episode_number=1, description="", season=season)
    return episode.id


class TestEpisode(TestCase):
    def test_episode_can_be_created(self):
        episode_id = create_episode("Test Title")

        episode = Episode.objects.get(id=episode_id)
        self.assertEqual(episode.season.number, 1)
        self.assertEqual(episode.title, "Test Title")
        self.assertEqual(episode.episode_number, 1)

    def test_episode_to_string(self):
        episode_id = create_episode("Test Title")
        episode = Episode.objects.get(id=episode_id)

        self.assertEqual(str(episode), "S01E01 - Test Title")
