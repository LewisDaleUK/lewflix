from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    image_url = models.CharField(max_length=512)
    video_location = models.CharField(max_length=512)

    def __str__(self):
        return "{} ({})".format(self.title, self.year)
