import datetime
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Todo
from accounts.models import CustomUser


# Create your views here.
@login_required
def list_todo_items(request):
    user = CustomUser.objects.get(email=request.user.email)  # Access username correctly
    todos = Todo.objects.filter(createdBy=user)  # Use filter instead of all
    return render(request, 'todos/todo_dashboard.html', {'user': user, 'todos': todos})

# class TodoListView(ListView):
#     return render(request, 'todos/list_todo_items.html')

@login_required
def add_todo_item(request:HttpRequest):   
    if request.method == 'POST':
        content = request.POST['content']
        
        # Create an instance of the Todo model
        todo = Todo()
        todo.content = content
        todo.createdBy = CustomUser.objects.get(email=request.user.email)
        todo.save()
        
    return redirect('list_todo_items')

@login_required
def delete_todo_item(request, id):
    Todo.objects.get(id=id).delete()
    return redirect('list_todo_items')