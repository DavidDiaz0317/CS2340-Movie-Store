# Generated by Django 5.1.4 on 2025-02-06 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_movie_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User', models.CharField(max_length=200)),
                ('MovieList', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User', models.CharField(max_length=200)),
                ('Body', models.CharField(max_length=200)),
            ],
        ),
    ]
