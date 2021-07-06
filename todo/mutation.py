import graphene
from todo.models import Todo
from todo.types import TodoType
from django.contrib.auth.models import User


class DeleteTodoMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    # The class attributes define the response of the mutation
    todo = graphene.Field(TodoType)
    success = graphene.Boolean()
    message = graphene.String()

    @classmethod
    def mutate(cls, self, info, id):
        try:
            todo = Todo.objects.get(pk=id)
            success = True
            message = f'Successfully deleted TODO: {id}'
            todo.delete()
        except Todo.DoesNotExist:
            todo = None
            success = False
            message = f'There is no todo with ID of {id}'
            # Notice we return an instance of this mutation

        return DeleteTodoMutation(todo=todo, success=success, message=message)


class AddTodoMutation(graphene.Mutation):
    class Arguments:
        body = graphene.String(required=True)
        userId = graphene.ID(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    @staticmethod
    def is_duplicate(body):
        if Todo.objects.filter(body=body).exists():
            return True
        else:
            return False

    @staticmethod
    def is_user_found(user):
        if User.objects.filter(pk=user.id):
            return True
        else:
            return False

    @classmethod
    def mutate(cls, root, info, body, userId):
        import json
        print(json.dumps(root))
        try:
            if cls.is_duplicate(body):
                success = False
                message = 'There is already a TODO with this body'
            else:
                user = User.objects.get(pk=userId)
                todo = Todo(body=body, user=user)
                todo.save()
                success = True
                message = "Successfully added TODO"
        except Todo.ValidationError:
            success = False
            message = "Could not create TODO"

        return AddTodoMutation(success=success, message=message)


class TodoMutation(graphene.ObjectType):
    delete_todo = DeleteTodoMutation.Field()
    add_todo = AddTodoMutation.Field()
