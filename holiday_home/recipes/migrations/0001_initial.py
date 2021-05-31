# Generated by Django 3.2.3 on 2021-05-31 19:43

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
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=177, unique=True)),
                ('slug', models.SlugField(max_length=177, unique=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='recipe_categories')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(allow_unicode=True)),
                ('instructions', models.TextField()),
                ('about', models.TextField(blank=True, default='')),
                ('image', models.ImageField(blank=True, upload_to='recipes')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='recipes.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='recipes.recipe')),
            ],
        ),
    ]
