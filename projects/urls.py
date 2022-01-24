from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name="projects"),
    path('project/<str:pk>/', views.project, name="project"),

    path('create-project/', views.create_pokemon, name="create_project"),
    path('update_pokemon/<str:pk>/', views.update_pokemon, name="update_pokemon"),
    path('delete_pokemon/<str:pk>/', views.delete_pokemon, name="delete_pokemon"),

]