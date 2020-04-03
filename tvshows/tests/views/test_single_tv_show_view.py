from django.test import TestCase
from django.urls import reverse

from tvshows.tests.helpers import create_tv_show, create_random_seasons


class SingleTVShowViewTests(TestCase):
    def test_displays_404_if_tv_show_does_not_exist(self):
        response = self.client.get(reverse('tvshows:tvshow', kwargs={'tv_show': 1}))
        self.assertEqual(response.status_code, 404)

    def test_displays_no_seasons_if_tv_show_has_no_associated_seasons(self):
        tv_show = create_tv_show('Test TV Show', 2012, 'http://fake-image-url')
        response = self.client.get(reverse('tvshows:tvshow', kwargs={'tv_show': tv_show.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no seasons available for this TV show")

    def test_displays_tv_seasons_if_found(self):
        tv_show = create_tv_show('Test TV Show', 1985, 'http://fake-image-url')
        seasons = create_random_seasons(tv_show)

        response = self.client.get(reverse('tvshows:tvshow', kwargs={'tv_show': tv_show.id}))

        for season in seasons:
            expected_url = reverse('tvshows:season', kwargs={'tv_show': tv_show.id, 'season': season.number})
            self.assertContains(response, 'Season ' + str(season.number))
            self.assertContains(response, expected_url)
