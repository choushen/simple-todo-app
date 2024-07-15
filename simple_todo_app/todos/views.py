from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from .models import Todo


# Create your views here.
def list_todo_items(request):
    return render(request, 'todos/todo_dashboard.html')

# class TodoListView(ListView):
#     return render(request, 'todos/list_todo_items.html')