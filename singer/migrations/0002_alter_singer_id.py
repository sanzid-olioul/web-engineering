# Generated by Django 4.2.6 on 2023-10-05 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singer',
            name='id',
            field=models.SlugField(editable=False, primary_key=True, serialize=False),
        ),
    ]