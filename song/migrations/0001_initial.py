# Generated by Django 4.2.6 on 2023-10-05 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions
import song.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('song_title', models.CharField(max_length=250)),
                ('song', models.FileField(upload_to=song.models.file_directory_path)),
                ('song_duration', models.CharField(blank=True, editable=False, max_length=50, null=True)),
                ('song_extension', models.CharField(blank=True, editable=False, max_length=10, null=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('song_album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='album.album')),
            ],
            options={
                'unique_together': {('song_title', 'song_album')},
            },
        ),
        migrations.CreateModel(
            name='SongLikedBy',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('date_likes', models.DateTimeField(auto_now_add=True)),
                ('song', models.ForeignKey(on_delete=django.db.models.expressions.Case, to='song.song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'SongsLikedBy',
                'ordering': ['-date_likes'],
                'unique_together': {('song', 'user')},
            },
        ),
        migrations.CreateModel(
            name='RecentlyPlayed',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('date_played', models.DateTimeField(auto_now_add=True)),
                ('song', models.ForeignKey(on_delete=django.db.models.expressions.Case, to='song.song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'RecentlyPlayed',
                'ordering': ['-date_played'],
                'unique_together': {('song', 'user')},
            },
        ),
    ]
