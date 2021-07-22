import graphene
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import graphene
import graphql_jwt
from graphql_jwt.shortcuts import get_token


def is_authenticated(user):
    if user.is_anonymous:
        raise Exception('You must be logged to vote!')
class CreateUserMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    success = graphene.Boolean()
    message = graphene.String()
    token = graphene.String()

    @classmethod
    def mutate(cls, self, info, username, password):
        try:
            user = User.objects.create_user(username=username, password=password)
            success = True
            message = "Successfully created user"
            token = get_token(user)
        except User.MultipleObjectsReturned:
            success = False
            message = "An error occured creating the user"
        return CreateUserMutation(success=success, message=message, token=token)

class UpdateContactInfoNameMutation(graphene.Mutation):

    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, first_name, last_name, email):

        try:
            # user = info.user.context Why doesn't it like scoping this to a variable?
            is_authenticated(info.context.user)
            user = User.objects.get(pk=info.context.user.id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()
            success = True
            message = f'Successfully updated user contact info'
        except User.MultipleObjectsReturned:
            success = False
            message = "An error occured updating user first name"
        
        return UpdateContactInfoNameMutation(success=success, message=message)
class UserMutation(graphene.ObjectType):
    create_user = CreateUserMutation.Field()
    update_contact_info = UpdateContactInfoNameMutation.Field()
    login_user = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
