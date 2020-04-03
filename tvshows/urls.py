from django.urls import path

from . import views

app_name='tvshows'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:tv_show>', views.get_tv_show, name='tvshow'),
    path('<int:tv_show>/season/<int:season>', views.get_season, name='season'),
    path('<int:tv_show>/season/<int:season>/episode/<int:episode>', views.get_episode, name='episode'),
]
