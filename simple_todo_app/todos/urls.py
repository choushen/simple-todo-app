from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_todo_items, name='list_todo_items'),
    path('add_todo/', views.add_todo_item, name='add_todo_item'),
    path('delete_todo/<int:id>/', views.delete_todo_item, name='delete_todo_item'),
]
