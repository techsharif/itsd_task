from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.utils import timezone


class Person(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username


class Task(models.Model):
    person = models.ForeignKey(Person)
    task_title = models.TextField()
    the_date = models.DateField(default=timezone.now)

    def __str__(self):
        return '{} : {} - ( {} )'.format(self.the_date, self.task_title, self.person)
