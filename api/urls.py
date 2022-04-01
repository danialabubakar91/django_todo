from django.urls import path
from todo import views
from . import views

urlpatterns = [
    path('todos', views.TodoListCreate.as_view()),
    path('todos/<int:pk>', views.TodoRetrieveUpdateDestroy.as_view()),
    path('todos/completed', views.TodoCompletedList.as_view()),
]
