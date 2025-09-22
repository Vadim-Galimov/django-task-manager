from django.urls import path
from . import views

urlpatterns = [

    path('', views.index , name='home'),
    path('all_tasks', views.all_tasks, name='all_tasks'),
    path('add_task', views.add_task, name='add_task'),
    path('delete_task/<int:task_id>', views.delete_task, name='delete_task'),
    path('edit_task/<int:task_id>', views.edit_task, name='edit_task'),
    path('start_new_day', views.start_new_day, name='start_new_day'),
    path('complete_task/<int:task_id>', views.complete_task, name='complete_task'),
]