# Generated by Django 3.0.6 on 2020-05-21 11:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import movies.models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20200521_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='episodes', to='movies.Movie', verbose_name='Аниме'),
        ),
        migrations.AlterField(
            model_name='episode',
            name='number',
            field=models.PositiveSmallIntegerField(verbose_name='Серия'),
        ),
        migrations.AlterField(
            model_name='episode',
            name='season',
            field=models.PositiveSmallIntegerField(verbose_name='Сезон'),
        ),
        migrations.AlterField(
            model_name='episode',
            name='title',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Название серии (если есть)'),
        ),
        migrations.AlterField(
            model_name='episode',
            name='video_obj',
            field=models.FileField(upload_to=movies.models.get_episode_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['webm', 'mkv', 'flv', 'avi', 'wmv', 'mp4'])], verbose_name='Видео'),
        ),
    ]
