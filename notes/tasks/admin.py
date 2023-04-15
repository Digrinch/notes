from django.contrib import admin
from tasks.models import Task
from django.contrib import admin


class AdminTask(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'author', 'deadline')
    search_fields = ('name',)
    empty_value_display = '----'

    class Meta:
        ordering = ('deadline', 'name')


admin.site.register(Task, AdminTask)
