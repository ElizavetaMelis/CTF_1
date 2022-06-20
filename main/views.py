from .forms import RegistrationForm
from .models import Task, Student
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView


def index(request):
    return render(request, "index.html", {})


# tasks view
def task(request):
    object = Task.objects.all()
    count = Task.objects.all().count()
    context = {
        "tasks" : object,
        "count" : count
    }

    return render(request, "task.html", context)


def task_1(request):
    return render(request, 'tasks/task-1.html', {})


def register_page(request):
    return render(request, "register.html")

def register_success(request):
    return render(request, "register_success.html")

class RegistrationView(CreateView):
    model = Student
    form_class = RegistrationForm
    # if form_class.is_valid(raise_exception=True):
    #     form_class.save()
    #     template_name = 'register_success.html'
    #     success_url = reverse_lazy('success_register')
    template_name = 'register.html'
    success_url = reverse_lazy('index')


