from django.urls import path

from . import views

app_name='movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.get_movie, name='get_movie')
]
