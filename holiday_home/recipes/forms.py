from . import models
from django import forms


class RecipeForm(forms.ModelForm):
    class Meta:
        fields = ('category', 'title', 'name', 'amount', 'instructions', 'about', 'image')
        models = models.Recipe

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields['category'].queryset = (
                models.Category.objects.filter(
                    pk__in=user.category.values_list('group__pk')
                )
            )
