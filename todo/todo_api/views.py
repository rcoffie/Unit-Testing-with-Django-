from todo.todo_api.serializers import  TodoSerializer
from todo.models import Todo
from rest_framework.response import Response
from rest_framework import generics

class ListTodo(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class UpdateTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
