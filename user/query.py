import graphene
from user.models import User
from user.types import UserType
from todo.types import TodoType


class UserQuery(graphene.ObjectType):
    get_user = graphene.Field(UserType, id=graphene.ID(required=True))
    get_users_todos = graphene.List(
        TodoType, first_name=graphene.String(required=True))

    def resolve_get_user(self, info, id):
        return User.objects.get(pk=id)

    def resolve_get_users_todos(self, info, first_name):
        try:
            user = User.objects.get(first_name=first_name)
        except User.DoesNotExist:
            return None

        return user.todo_set.all()
