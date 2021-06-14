from graphene_django import DjangoObjectType
from todo.models import Todo


class TodoType(DjangoObjectType):

    class Meta:
        # Reference the model you are accessing
        model = Todo
        fields = ('body', 'last_modified', 'id')
