import graphene
from django.contrib.auth.models import User
from user.types import UserType
from todo.types import TodoType


class UserQuery(graphene.ObjectType):
    get_user = graphene.Field(UserType, id=graphene.ID(required=True))
    get_users_todos = graphene.List(
        TodoType, id=graphene.String(required=True))
    get_all_users = graphene.Field(graphene.List(UserType))

    def resolve_get_user(self, info, id):
        return User.objects.get(pk=id)

    def resolve_get_users_todos(self, info, id):
        try:
            user = User.objects.get(pk=id)
        except User.DoesNotExist:
            return None

        return user.todo_set.all()
    
    def resolve_get_all_users(self, info):
        return User.objects.all()
