from . import models
from django import forms
from django.forms.models import inlineformset_factory


class RecipeIngredientsForm(forms.ModelForm):

    class Meta:
        model = models.RecipeIngredients
        exclude = ()


RecipeIngredientsFormSet = inlineformset_factory(
    models.Recipe, models.RecipeIngredients, form=RecipeIngredientsForm,
    fields=['name', 'amount'], extra=1, can_delete=True)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = models.Recipe
        fields = ['category', 'title', 'image', 'instructions', 'about']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields['category'].queryset = (
                models.Category.objects.filter(
                    pk__in=user.category.values_list('category__pk')
                )
            )




