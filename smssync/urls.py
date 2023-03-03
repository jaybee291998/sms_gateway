from django.urls import path
from . import views

urlpatterns = [
    path('', views.task, name='task'),
    path('post-task/', views.post_task, name='post_task')
]
