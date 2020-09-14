from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_todo/', views.add, name='add'),
    path('delete_todo/<int:todo_id>/', views.delete, name='delete'),
]