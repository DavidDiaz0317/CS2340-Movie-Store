# Generated by Django 5.1.5 on 2025-02-11 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0004_alter_movie_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='Price',
            field=models.IntegerField(default=10),
        ),
    ]
