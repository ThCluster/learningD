from django.urls import path, include # 
from rest_framework import routers
from todo.viewsets.todo_viewsets import TodoViewSet
from todo.viewsets.todolist_viewsets import TodoListViewSet

default_router = routers.DefaultRouter()

default_router.register(r'todos', TodoViewSet, basename='todos')
default_router.register(r'todolists', TodoListViewSet, basename='todolists')  

urlpatterns = [
    path('', include(default_router.urls)),
    path('auth/', include('dj_rest_auth.urls')),
]
