import graphene
from django.contrib.auth.models import User


class CreateUserMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    @classmethod
    def mutate(cls, self, info, username, password):
        try:
            User.objects.create_user(username=username, password=password).save()
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


class UserMutation(graphene.ObjectType):
    create_user = CreateUserMutation.Field()
    update_contact_info = UpdateContactInfoNameMutation.Field()
