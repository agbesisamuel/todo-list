from django.urls import path

from .views import *

app_name = 'todo'
urlpatterns = [
    path('', home, name="home"),
    path('add', add_todo, name="add_todo"),
    path('delete/<pk>', delete_todo, name="delete_todo"),
    path('complete/<pk>', complete_todo, name="complete_todo")
]
