from django.urls import path
from tasks.apps import TasksConfig
from tasks.views import index, task_in_work, task_done, task_delete, task_create, task_edit

app_name = TasksConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('tasks/<int:task_id>/work/', task_in_work, name='take'),
    path('tasks/<int:task_id>/done/', task_done, name='done'),
    path('tasks/<int:task_id>/delete/', task_delete, name='delete'),
    path('tasks/create/', task_create, name='create'),
    path('tasks/<int:task_id>/edit/', task_edit, name='edit'),
]
