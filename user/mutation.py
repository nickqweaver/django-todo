import graphene
from user.models import User


class CreateUserMutation(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        age = graphene.Int(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    @classmethod
    def mutate(cls, self, info, first_name, last_name, age):
        try:
            User(first_name=first_name, last_name=last_name, age=age).save()
            success = True
            message = "Successfully created user"
        except User.ValidationError:
            success = False
            message = "An error occured creating the user"

        return CreateUserMutation(success=success, message=message)


class UserMutation(graphene.ObjectType):
    create_user = CreateUserMutation.Field()
