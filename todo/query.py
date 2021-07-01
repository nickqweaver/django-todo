import graphene
from todo.types import TodoType
from todo.models import Todo


class TodoQuery(graphene.ObjectType):
    all_todos = graphene.List(TodoType)
    get_todo_by_id = graphene.Field(TodoType, id=graphene.ID(required=True))

    def resolve_all_todos(root, info):
        return Todo.objects.all()

    def resolve_get_todo_by_id(self, info, id):
        try:
            return Todo.objects.get(id=id)
        except Todo.DoesNotExist:
            return None
