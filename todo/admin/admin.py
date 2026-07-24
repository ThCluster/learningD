from django.contrib import admin

from todo.models.todo import Todo
from todo.models.todolist import TodoList

# Register your models here.

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ("title", "completed", "favorite", "todolist")
    list_filter = ("completed", "favorite", "todolist")
    search_fields = ("title",)
    ordering = ("title",)
    readonly_fields = ('current_date',) 

    

@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ("name",)
 