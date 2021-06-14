from django.contrib import admin
from todo.models import Todo
# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    fields = ['body']


admin.site.register(Todo, TodoAdmin)
