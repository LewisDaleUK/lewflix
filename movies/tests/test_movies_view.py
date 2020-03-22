from django.test import TestCase
from django.urls import reverse

from movies.models import Movie


def create_movie(title, year, image_url):
    Movie.objects.create(title=title, year=year, image_url=image_url)


class MoviesViewTests(TestCase):
    def test_index_returns_no_movies_message_when_no_movies_available(self):
        response = self.client.get(reverse('movies:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no movies currently available")

    def test_index_displays_a_movie_when_available(self):
        create_movie("Test Movie", 2012, "http://fake-image-url")
        response = self.client.get(reverse('movies:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Movie (2012)")
