from django.urls import path

from rest_framework import routers

from .views import (
    TodoAPIViewset,
    TodoAPICreateView
)

router = routers.DefaultRouter()
router.register(r'todos', TodoAPIViewset)

urlpatterns = [
    path('todos/add', TodoAPICreateView.as_view(), name="create_todo_api")
]

urlpatterns += router.urls
