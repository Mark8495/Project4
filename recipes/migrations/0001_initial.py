# Generated by Django 3.2.15 on 2022-09-17 21:10

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mealtime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='breakfast', max_length=250, null=True, unique=True)),
                ('slug', models.SlugField(default='breakfast', max_length=250, null=True, unique=True)),
                ('mealtime_image', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='mealtime')),
            ],
        ),
        migrations.CreateModel(
            name='Preptime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preptime_image', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='preptime')),
                ('title', models.CharField(default='placeholder', max_length=250, null=True, unique=True)),
                ('slug', models.SlugField(default='placeholder', max_length=250, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('serving_size', models.CharField(default=0, max_length=30)),
                ('ingredients', models.TextField(blank=True)),
                ('instructions', models.TextField(blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_posts', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='recipe_likes', to=settings.AUTH_USER_MODEL)),
                ('mealtime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_posts', to='recipes.mealtime')),
                ('preptime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_posts', to='recipes.preptime')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='recipes.recipe')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]