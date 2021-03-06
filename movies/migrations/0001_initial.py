# Generated by Django 3.0.6 on 2020-05-18 22:23

from django.db import migrations, models
import django.db.models.deletion
import movies.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('movie_picture', models.ImageField(upload_to=movies.models.get_movie_image_path)),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_obj', models.FileField(upload_to=movies.models.get_episode_path)),
                ('number', models.PositiveSmallIntegerField()),
                ('season', models.PositiveSmallIntegerField()),
                ('name', models.CharField(max_length=128)),
                ('movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.Movie')),
            ],
        ),
    ]
