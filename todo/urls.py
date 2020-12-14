from django.urls import path
from .views import TodoListView, TodoCreateView,TodoUpdateView, TodoDeleteView

urlpatterns = [
    path("delete/<int:pk>/", TodoDeleteView.as_view(), name="del"),
    path('new/', TodoCreateView.as_view(), name='todo_new'),
    path("edit/<int:pk>/",TodoUpdateView.as_view(), name="todo_edit"),
    path('', TodoListView.as_view(), name="home"),
]