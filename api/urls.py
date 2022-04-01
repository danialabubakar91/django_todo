from django.urls import path
from todo import views
from . import views

urlpatterns = [
    path('todos/completed', views.TodoCompletedList.as_view()),
]
