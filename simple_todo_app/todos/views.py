from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, DeleteView
from .models import Todo
from accounts.models import CustomUser


# Create your views here.
@login_required
def list_todo_items(request):
    user = CustomUser.objects.get(username=request.user.email)  # Access username correctly
    todos = Todo.objects.filter(createdBy=user)  # Use filter instead of all
    return render(request, 'todos/todo_dashboard.html', {'user': user, 'todos': todos})

# class TodoListView(ListView):
#     return render(request, 'todos/list_todo_items.html')