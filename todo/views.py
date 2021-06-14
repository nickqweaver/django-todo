from django.shortcuts import render
from django.views import generic
from todo.models import Todo
# Create your views here.


class IndexView(generic.ListView):
    template_name = "todo/index.html"
    context_object_name = 'todo_list'

    def get_queryset(self):
        return Todo.objects.order_by("-last_modified")[:5]
