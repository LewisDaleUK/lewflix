# Generated by Django 3.0.4 on 2020-03-22 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='video_location',
            field=models.CharField(max_length=512, null=True),
        ),
    ]