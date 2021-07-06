from graphene_django import DjangoObjectType
from django.contrib.auth.models import User



class UserType(DjangoObjectType):

    class Meta:
        # Reference the model you are accessing
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'todo_set')
