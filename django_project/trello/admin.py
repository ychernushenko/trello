from django.contrib import admin
from trello.models import Task
from trello.models import Status 

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'status')
    fieldsets = [
        (None,          {'fields': ['task_name']}),
        (None,          {'fields': ['status']})
    ]

class StatusAdmin(admin.ModelAdmin):
    list_display = ['status_name']
    fieldsets = [
        (None,          {'fields': ['status_name']})
    ]

admin.site.register(Task, TaskAdmin)
admin.site.register(Status, StatusAdmin)
