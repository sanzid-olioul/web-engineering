# Generated by Django 4.2.6 on 2023-10-16 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='album',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='albumlikedby',
            unique_together=set(),
        ),
    ]
