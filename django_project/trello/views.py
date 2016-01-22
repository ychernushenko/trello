from django.shortcuts import render
from trello.models import Status
from trello.models import Task

def index(request):
    status_list = Status.objects.all()
    task_list = Task.objects.all()
    context = {'status_list': status_list,
               'task_list': task_list
    }
    return render(request, 'trello/index.html', context)
