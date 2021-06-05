from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.urls import reverse_lazy

from .models import Category, Recipe, RecipeIngredients
from .forms import RecipeForm, RecipeIngredientsFormSet

User = get_user_model()


class ListCategory(generic.ListView):
    model = Category
    template_name = 'all_categories.html'


class SingleCategory(generic.DetailView):
    model = Category
    template_name = 'category_detail.html'


class SingleRecipe(generic.DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'


class MyRecipeList(LoginRequiredMixin, generic.ListView):
    model = Recipe
    template_name = 'my_recipes.html'

    def get_queryset(self):
        return Recipe.objects.filter(user=self.request.user)


class UserRecipeList(generic.ListView):
    model = Recipe
    template_name = 'user_recipes'

    def get_queryset(self):
        try:
            self.user_recipes = User.objects.prefetch_related('recipes').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.user_recipes.recipes.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_recipes'] = self.user_recipes
        return context


class CreateRecipe(LoginRequiredMixin, generic.CreateView):

    form_class = RecipeForm
    template_name = 'recipe_form.html'

    def get_context_data(self, **kwargs):
        data = super(CreateRecipe, self).get_context_data(**kwargs)
        if self.request.POST:
            data['ingredients'] = RecipeIngredientsFormSet(self.request.POST)
        else:
            data['ingredients'] = RecipeIngredientsFormSet()
        return data

    def from_valid(self, form):
        context = self.get_context_data()
        ingredients = context['ingredients']
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        if ingredients.is_valid():
            ingredients.instance = self.object
            ingredients.save()
        return super().form_valid(form)


class DeleteRecipe(LoginRequiredMixin, generic.DeleteView):

    model = Recipe
    success_url = reverse_lazy('recipes:my_recipes')
