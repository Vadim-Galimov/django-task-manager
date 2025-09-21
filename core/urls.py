from django.urls import path
from . import views

urlpatterns = [

    path('', views.index , name='home'),
    path('all_tasks', views.all_tasks, name='all_tasks'),
    path('add_task', views.add_task, name='add_task'),
]