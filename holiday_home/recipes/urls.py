from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.ListCategory.as_view(), name='all_categories'),
    path('categories/<slug:slug>', views.SingleCategory.as_view(), name='single_category'),
    path('new/', views.CreateRecipe.as_view(), name='add_recipe'),
    path('<username>/', views.MyRecipeList.as_view, name='my_recipes'),
    path('<username>/recipes/', views.UserRecipeList.as_view(), name='user_recipes'),
    path('<slug:slug>/<int:pk>', views.SingleRecipe.as_view(), name='single_recipe'),
    path('delete/<slug:slug>/<int:pk>', views.DeleteRecipe.as_view(), name='delete_recipe')

]