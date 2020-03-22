from django.test import TestCase
from django.urls import reverse

from movies.models import Movie


def create_movie(title, year, image_url, video_location):
    return Movie.objects.create(title=title, year=year, image_url=image_url, video_location=video_location)


class MovieDetailsTest(TestCase):
    def test_index_returns_404_if_movie_does_not_exist(self):
        response = self.client.get(reverse('movies:get_movie', args=[1234]))
        self.assertEqual(response.status_code, 404)

    def test_movie_is_retrieved_if_movie_exists(self):
        movie = create_movie("Test Movie", 2012, "http://fake-url", "/a/fake/path")
        response = self.client.get(reverse('movies:get_movie', args=[movie.id]))
        self.assertEqual(response.status_code, 200)