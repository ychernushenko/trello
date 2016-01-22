from django.db import models

class Status(models.Model):
    status_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.status_name

class Task(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=200)
