import graphene
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

## 39228ceee11517acafec4ad5e805ee92888b7560
class CreateUserMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    @classmethod
    def mutate(cls, self, info, username, password):
        try:
            User.objects.create_user(username=username, password=password)
            success = True
            message = "Successfully created user"
        except User.MultipleObjectsReturned:
            success = False
            message = "An error occured creating the user"

        return CreateUserMutation(success=success, message=message)

class UpdateContactInfoNameMutation(graphene.Mutation):

    class Arguments:
        id = graphene.ID(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, id, first_name, last_name, email):
        try:
            user = User.objects.get(pk=id)
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

class LoginUserMutation(graphene.Mutation):

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    token = graphene.String()
    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, username, password):
        user = authenticate(username=username, password=password)
        if user is not None:
            login(info.context, user)
            token, _ = Token.objects.get_or_create(user=user)
            message = "Successfully logged in"
            return LoginUserMutation(success=True, message=message, token=token)
        else:
            return LoginUserMutation(success=False, message="User could not be Authenticate")
            
class LogoutUserMutation(graphene.Mutation):
    success = graphene.NonNull(graphene.Boolean)

    @staticmethod
    def mutate(root, info):
        logout(info.context)
        return LogoutUserMutation(success=True)


class UserMutation(graphene.ObjectType):
    create_user = CreateUserMutation.Field()
    update_contact_info = UpdateContactInfoNameMutation.Field()
    login_user = LoginUserMutation.Field()
    logout_user = LogoutUserMutation.Field()
