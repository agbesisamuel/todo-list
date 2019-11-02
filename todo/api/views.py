from django.shortcuts import Http404

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import (
    TodoCreateSerializer,
    TodoListDetailSerializer
)

from ..models import Todo


class TodoAPICreateView(CreateAPIView):
    """
    Create a todo task
    """
    permission_classes = [AllowAny]
    serializer_class = TodoCreateSerializer
    queryset = Todo.objects.all()


class TodoAPIViewset(viewsets.ModelViewSet):
    """
    Returns a list of all todo task
    Also, retrieve, update and deletes a todo task
    """
    permission_classes = [AllowAny]
    queryset = Todo.objects.all()
    serializer_class = TodoListDetailSerializer
    allowed_methods = ['GET', 'PUT', 'DELETE']
