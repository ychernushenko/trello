# -*- coding: utf-8 -*-
from django.db import models

class Status(models.Model):
    STATUS_CHOICES = (
        ('New', 'New'),
        ('InProgress', 'InProgress'),
        ('OnReview', 'OnReview'),
        ('Tested', 'Tested'),
        ('Delivered', 'Delivered')
    )

    # custom error message in russian
    default_error_messages = {
        'unique': 'Данный статус ужe существует',
    }

    status_name = models.CharField(max_length=200, choices = STATUS_CHOICES, unique=True, error_messages=default_error_messages)

    def __unicode__(self):
        return self.status_name

class Task(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=200)
