from django.db import models
from django.utils.translation import gettext_lazy as _

from base.utils.models.standard_models import StandardModel
from todo.models.todolist import TodoList

# Create your models here.

class Todo(StandardModel):
    """
    Model representing a Todo item.
    """
    
    class Meta:
        verbose_name = _("Todo")
        verbose_name_plural = _("Todos")
        
    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name="todos", verbose_name=_("TodoList"))
    current_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Current Date"))
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    completed = models.BooleanField(default=False, verbose_name=_("Completed"))
    favorite = models.BooleanField(default=False, verbose_name=_("Favorite"))
    
    def __str__(self):
        return self.title 