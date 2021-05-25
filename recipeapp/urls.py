from  django.urls import path
from recipeapp import views

urlpatterns=[
    path('',views.index,name="index"),
    path('recipe_list/',views.recipeList,name="recipe_list"),
    path('recipe_detail/',views.recipeDetail,name="recipe_detail"),
]
