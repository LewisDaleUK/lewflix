from django.test import TestCase
from django.urls import reverse

from tvshows.tests.helpers import create_tv_show


class TVShowViewTests(TestCase):
    def test_index_returns_no_tv_shows_message_when_no_tv_shows_available(self):
        response = self.client.get(reverse('tvshows:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no TV shows currently available")

    def test_index_displays_a_tv_show_when_available(self):
        create_tv_show("Test TV Show", 2012, "http://fake-image-url")
        response = self.client.get(reverse('tvshows:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test TV Show")
        self.assertContains(response, "(2012)")
        self.assertContains(response, "src=\"http://fake-image-url\"")

    def test_index_links_to_tv_show_view(self):
        tv_show = create_tv_show("Fake TV Show", 2020, "http://fake-image-url")
        expected_url = reverse('tvshows:tvshow', kwargs={'tv_show': tv_show.id})
        response = self.client.get(reverse('tvshows:index'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, expected_url)
