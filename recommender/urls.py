from django.urls import path
from . import views

urlpatterns = [

        path('',views.allrecipes,name='recipes'),
        path('<int:p>',views.recipespage,name='recipes'),
        path('<str:title>',views.recipes,name='search'),
        path('recipe/<str:id>',views.getrecipe,name='getrecipe'),
        path('recommended/',views.recommend,name='recommend'),
        path('favorites/',views.getliked,name='getliked'),


]
