from graphene_django import DjangoObjectType
from user.models import User


class UserType(DjangoObjectType):

    class Meta:
        # Reference the model you are accessing
        model = User
        fields = ('first_name', 'last_name', 'age', 'todo_set')
