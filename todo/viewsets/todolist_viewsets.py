from rest_framework import viewsets
from todo.serializers.todolist_serializers import TodoListSerializer
from todo.models.todolist import TodoList

# Create your viewsets here.


class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    filterset_fields = ['name']