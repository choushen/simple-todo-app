from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from .models import Todo


# Create your views here.
def list_todo_items(request):
    return HttpResponse('Todo list')

# class TodoListView(ListView):
#     return render(request, 'todos/list_todo_items.html')