from django.shortcuts import render
from django.http import HttpResponse
from trello.models import Status
from trello.models import Task
import json

def index(request):
    status_list = Status.objects.all()
    task_list = Task.objects.all()
    context = {'status_list': status_list,
               'task_list': task_list
    }
    return render(request, 'trello/index.html', context)

def ajax(request):
    selected_task = Task.objects.get(pk=request.POST['task_id'])
    selected_status = Status.objects.get(pk=request.POST['status_id'])
    selected_task.status = selected_status
    selected_task.save()
    return HttpResponse(json.dumps({'status': 'OK'}), content_type="application/json")
