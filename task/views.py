import datetime

from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic.base import View

from task.models import Task, Person
from collections import OrderedDict


class TaskAllVIew(View):
    template_name = 'task_all.html'

    def get(self, request):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/login/')
        person = get_object_or_404(Person, user=request.user)
        all = request.GET.get('all', False)
        if all:
            tasks = Task.objects.all()
        else:
            tasks = Task.objects.filter(the_date__gte=datetime.date.today())
        result = dict()
        for task in tasks:
            dt = str(task.the_date)
            person = task.person.user.username
            if dt in result.keys():
                if person in result[dt].keys():
                    result[dt][person] += [task]
                else:
                    result[dt][person] = [task]
            else:
                result[dt] = dict()
                result[dt][person] = [task]

        return render(request, self.template_name, {'tasks': OrderedDict(sorted(result.items()))})


class TaskVIew(View):
    template_name = 'task.html'

    def get(self, request):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/login/')
        person = get_object_or_404(Person, user=request.user)

        all = request.GET.get('all', False)
        if all:
            tasks = Task.objects.filter(person=person)
        else:
            tasks = Task.objects.filter(person=person, the_date__gte=datetime.date.today())

        result = dict()
        for task in tasks:
            dt = str(task.the_date)
            if dt in result.keys():
                result[dt] += [task]
            else:
                result[dt] = [task]
        return render(request, self.template_name, {'tasks': OrderedDict(sorted(result.items()))})

    def post(self, request):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/login/')
        person = get_object_or_404(Person, user=request.user)
        task_title = request.POST.get('task_title')
        the_date = request.POST.get('the_date')

        try:
            Task(person=person,task_title=task_title,the_date=the_date).save()
        except:
            pass
        return HttpResponseRedirect('/')
