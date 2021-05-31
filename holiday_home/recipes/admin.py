from django.contrib import admin
from .models import Category, Recipe, RecipeIngredients


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at', 'updated', 'category']
    list_filter = ['category', 'title', 'user', 'created_at', 'updated']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredients)
