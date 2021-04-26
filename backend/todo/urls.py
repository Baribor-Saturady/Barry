from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create_todo, name="create_todo"),
]
 