from django.test import TestCase
from django.urls import reverse

from tvshows.tests.helpers import create_tv_show, create_season, create_episode


class TestEpisodeView(TestCase):
    def test_404_if_tv_show_does_not_exist(self):
        response = self.client.get(reverse('tvshows:episode', kwargs={'tv_show': 1, 'season': 1, 'episode': 1}))
        self.assertEqual(response.status_code, 404)

    def test_404_if_season_does_not_exist(self):
        tv_show = create_tv_show('Test TV Show', 2020, 'http://fake-image')
        response = self.client.get(
            reverse('tvshows:episode', kwargs={'tv_show': tv_show.id, 'season': 1, 'episode': 1})
        )
        self.assertEqual(response.status_code, 404)

    def test_404_if_episode_does_not_exist(self):
        tv_show = create_tv_show('Test TV Show', 2020, 'http://fake-image')
        season = create_season(tv_show, 1)
        response = self.client.get(
            reverse('tvshows:episode', kwargs={'tv_show': tv_show.id, 'season': season.number, 'episode': 1})
        )
        self.assertEqual(response.status_code, 404)

    def test_displays_episode(self):
        tv_show = create_tv_show('Test TV Show', 2020, 'http://fake-image')
        season = create_season(tv_show, 1)
        episode = create_episode('TV Show Episode', 1, 'Test tv show description', season)
        response = self.client.get(
            reverse('tvshows:episode',
                    kwargs={'tv_show': tv_show.id, 'season': season.number, 'episode': episode.episode_number}
                    )
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, episode.title)
        self.assertContains(response, episode.episode_number)
        self.assertContains(response, episode.description)

    def test_displays_next_episode_link_if_later_episode(self):
        tv_show = create_tv_show('Test TV Show', 2020, 'http://fake-image')
        season = create_season(tv_show, 1)
        episode_one = create_episode('TV Show First', 1, 'Test tv show description', season)
        episode_two = create_episode('TV Show Second Episode', 2, 'Test tv show description', season)
        response = self.client.get(
            reverse('tvshows:episode',
                    kwargs={'tv_show': tv_show.id, 'season': season.number, 'episode': episode_one.episode_number}
                    )
        )

        expected_url = reverse('tvshows:episode', kwargs={'tv_show': tv_show.id,
                                                          'season': season.number,
                                                          'episode': episode_two.episode_number}
                               )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Next Episode")
        self.assertContains(response, expected_url)

    def test_displays_next_episode_link_if_later_episode_in_different_season(self):
        tv_show = create_tv_show('Test TV Show', 2020, 'http://fake-image')
        season_one = create_season(tv_show, 1)
        season_two = create_season(tv_show, 2)
        episode_one = create_episode('TV Show First', 1, 'Test tv show description', season_one)
        episode_two = create_episode('TV Show Second Episode', 1, 'Test tv show description', season_two)

        response = self.client.get(
            reverse('tvshows:episode',
                    kwargs={'tv_show': tv_show.id, 'season': season_one.number, 'episode': episode_one.episode_number}
                    )
        )

        expected_url = reverse('tvshows:episode', kwargs={'tv_show': tv_show.id,
                                                          'season': season_two.number,
                                                          'episode': episode_two.episode_number}
                               )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Next Episode")
        self.assertContains(response, expected_url)

    def test_displays_previous_episode_link_if_previous_episode(self):
        tv_show = create_tv_show('Test TV Show', 2020, 'http://fake-image')
        season = create_season(tv_show, 1)
        episode_one = create_episode('TV Show First', 1, 'Test tv show description', season)
        episode_two = create_episode('TV Show Second Episode', 2, 'Test tv show description', season)
        response = self.client.get(
            reverse('tvshows:episode',
                    kwargs={'tv_show': tv_show.id, 'season': season.number, 'episode': episode_two.episode_number}
                    )
        )

        expected_url = reverse('tvshows:episode', kwargs={'tv_show': tv_show.id,
                                                          'season': season.number,
                                                          'episode': episode_one.episode_number}
                               )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Previous Episode")
        self.assertContains(response, expected_url)

    def test_displays_previous_episode_link_if_earlier_episode_in_different_season(self):
        tv_show = create_tv_show('Test TV Show', 2020, 'http://fake-image')
        season_one = create_season(tv_show, 1)
        season_two = create_season(tv_show, 2)
        episode_one = create_episode('TV Show First', 1, 'Test tv show description', season_one)
        episode_two = create_episode('TV Show Second Episode', 1, 'Test tv show description', season_two)

        response = self.client.get(
            reverse('tvshows:episode',
                    kwargs={'tv_show': tv_show.id, 'season': season_two.number, 'episode': episode_two.episode_number}
                    )
        )

        expected_url = reverse('tvshows:episode', kwargs={'tv_show': tv_show.id,
                                                          'season': season_one.number,
                                                          'episode': episode_one.episode_number}
                               )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Previous Episode")
        self.assertContains(response, expected_url)
