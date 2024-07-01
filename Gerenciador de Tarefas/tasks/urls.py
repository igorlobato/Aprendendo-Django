from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('tasks/new/', views.task_create, name='task_create'),
    path('tasks/<int:task_id>/edit/', views.task_edit, name='task_edit'),
    path('tasks/<int:task_id>/delete/', views.task_delete, name='task_delete'),
    path('signup/', views.signup, name='signup'),
]
