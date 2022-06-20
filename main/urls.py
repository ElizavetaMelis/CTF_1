from unicodedata import name
from . import views
from django.urls import path

from .views import RegistrationView

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', views.task, name='task'),
    path('tasks/task-1/', views.task_1, name='task-1'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('register/register_success', RegistrationView.as_view(), name='success_register'),
]