import graphene
from django.contrib.auth.models import User
from user.types import UserType
from todo.types import TodoType

## Why can't this method live inside the UserQuery Class?
def is_authenticated(user):
    print("Here")
    if user.is_anonymous:
        raise Exception("You must be logged in!")
class UserQuery(graphene.ObjectType):
    get_user = graphene.Field(UserType)
    get_users_todos = graphene.List(TodoType)
    get_all_users = graphene.Field(graphene.List(UserType))

    def resolve_get_user(self, info):
        user = info.context.user
        is_authenticated(user)
        
        return user

    def resolve_get_users_todos(self, info):
        user = info.context.user
        is_authenticated(user)

        return user.todo_set.all()
    
    def resolve_get_all_users(self, info):
        return User.objects.all()
