from django.shortcuts import render
from django.views import generic
from todo.models import Todo
from django.shortcuts import render

# from django.http import HttpResponse
# from django.template import loader

# Create your views here.


class IndexView(generic.ListView):
    template_name = "todo/index.html"
    context_object_name = 'todo_list'

    def get_queryset(self):
        return Todo.objects.order_by("-last_modified")[:5]

## Refactor this to a generic view
def detail(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    # template = loader.get_template('todo/sick.html')
    ## This is how we are sending context into the HttpResponse, Graphene does it for us
    context = {
        "custom_val": "this is a custom value that is hard coded",
        "other_val": "This is the response motha trucka",
        "todo_body": todo.body
    }

    print(request)
    # return HttpResponse(template.render(context, request))
    ## Shortcut for the above 
    return render(request, 'todo/sick.html', {'context': context}) ## We are creating a dict called context and sending it through the response, or we can just send the context dict without a key

