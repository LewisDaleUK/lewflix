from django.test import TestCase
from django.urls import reverse

from tvshows.tests.helpers import create_tv_show, create_season, create_random_episodes


class TestSeasonView(TestCase):
    def test_throws_404_if_tv_show_and_season_does_not_exist(self):
        response = self.client.get(reverse('tvshows:season', kwargs={'tv_show': 1, 'season': 1}))
        self.assertEqual(response.status_code, 404)

    def test_throws_404_tv_show_exists_but_season_does_not(self):
        tv_show = create_tv_show('Test Show', 2012, 'http://fake-image-url')
        response = self.client.get(reverse('tvshows:season', kwargs={'tv_show': tv_show.id, 'season': 1}))
        self.assertEqual(response.status_code, 404)

    def test_displays_no_episodes_found(self):
        tv_show = create_tv_show('Test Show', 2012, 'http://fake-image-url')
        season = create_season(tv_show, 1)

        response = self.client.get(reverse('tvshows:season', kwargs={'tv_show': tv_show.id, 'season': season.number}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No episodes found for this season")

    def test_displays_list_of_found_episodes(self):
        tv_show = create_tv_show('Test Show', 2012, 'http://fake-image-url')
        season = create_season(tv_show, 1)
        episodes = create_random_episodes(season)

        response = self.client.get(reverse('tvshows:season', kwargs={'tv_show': tv_show.id, 'season': season.number}))
        self.assertEqual(response.status_code, 200)

        for episode in episodes:
            expected_url = reverse('tvshows:episode',
                                   kwargs={'tv_show': tv_show.id,
                                           'season': season.number,
                                           'episode': episode.episode_number}
                                   )
            self.assertContains(response, 'Episode ' + str(episode.episode_number))
            self.assertContains(response, episode.title)
            self.assertContains(response, expected_url)
