from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=177, unique=True)
    slug = models.SlugField(max_length=177, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='recipe_categories', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Recipe(models.Model):
    user = models.ForeignKey(User, related_name='recipe', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(allow_unicode=True)
    instructions = models.TextField(blank=False)
    about = models.TextField(blank=True, default='')
    image = models.ImageField(upload_to='recipes', blank=True)
    category = models.ForeignKey(Category, related_name='categories', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Recipe, self).save(*args, **kwargs)

    # add get_absolute_url


class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='recipes', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)

    def __str__(self):
        return self.name
