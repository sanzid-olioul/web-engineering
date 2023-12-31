# Generated by Django 4.2.6 on 2023-10-05 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.SlugField(primary_key=True, serialize=False)),
                ('singer_name', models.CharField(max_length=50)),
                ('singer_avater', models.ImageField(blank=True, null=True, upload_to='')),
                ('singer_bio', models.TextField()),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('birth_place', models.TextField()),
            ],
        ),
    ]
