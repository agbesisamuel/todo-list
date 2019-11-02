from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .models import Todo
from .forms import TodoForm


def home(request):
    todos = Todo.objects.all()
    form = TodoForm()
    template_name = 'todo/index.html'
    
    context = {
        'todos': todos,
        'form':form
    }
    
    return render(request, template_name, context)


@require_POST
def add_todo(request):
    form = TodoForm(request.POST)
    
    title = request.POST['title']
    todo = Todo.objects.create(title=title)
    todo.save()
    
    return redirect("todo:home")


def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()

    return redirect("todo:home")


def complete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    print(todo)
    todo.completed = True
    todo.save()

    return redirect("todo:home")
