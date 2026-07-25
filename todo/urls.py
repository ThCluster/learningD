from rest_framework.routers import DefaultRouter
from todo.viewsets.todo_viewsets import TodoViewSet
from todo.viewsets.todolist_viewsets import TodoListViewSet # <-- AJOUTEZ CET IMPORT

router = DefaultRouter()

# On enregistre les DEUX viewsets dans l'application todo
router.register(r'todos', TodoViewSet, basename='todos')
router.register(r'todolists', TodoListViewSet, basename='todolists') # <-- AJOUTEZ CETTE LIGNE

urlpatterns = router.urls
