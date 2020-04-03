from django.contrib import admin

from tvshows.models import TVShow, Season, Episode

admin.site.register(TVShow)
admin.site.register(Season)
admin.site.register(Episode)