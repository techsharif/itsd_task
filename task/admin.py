from django.contrib import admin

# Register your models here.
from task.models import Person, Task

admin.site.register(Person)
admin.site.register(Task)
