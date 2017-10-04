from django.conf.urls import url

from task.views import TaskAllVIew

urlpatterns = [
    url(r'^all/$', TaskAllVIew.as_view(), name='task_all'),
]
