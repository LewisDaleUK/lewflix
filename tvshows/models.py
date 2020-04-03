from django.db import models


# Create your models here.
class TVShow(models.Model):
    title = models.CharField(max_length=255)
    start_year = models.DateField()
    image_url = models.CharField(max_length=512)

    def __str__(self):
        return "{} ({})".format(self.title, self.start_year.year)


class Season(models.Model):
    number = models.IntegerField()
    tv_show = models.ForeignKey(TVShow, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number).zfill(2)


class Episode(models.Model):
    title = models.CharField(max_length=255)
    episode_number = models.IntegerField()
    description = models.TextField(blank=True)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    video_location = models.TextField(max_length=512)

    def __str__(self):
        formatted_episode = str(self.episode_number).zfill(2)
        return "S{}E{} - {}".format(str(self.season), formatted_episode, self.title)
