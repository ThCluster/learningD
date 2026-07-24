from rest_framework import viewsets
from todo.serializers import TodoSerializer
from todo.models.todo import Todo
# Create your viewsets here.


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filterset_fields = ['current_date','favorite','completed']
    search_fields = ['title']