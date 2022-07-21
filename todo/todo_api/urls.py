from django.urls import path
from todo.todo_api.views import ListTodo, UpdateTodo
urlpatterns = [
path('',ListTodo.as_view(),name='list_todo'),
path('<int:pk>/',UpdateTodo.as_view(), name='update_todo')

]
