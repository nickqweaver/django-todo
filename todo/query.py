import graphene
from todo.types import TodoType
from todo.models import Todo

### Querying any TODO data should require that the user must be logged in and only show
### That specifc users TODO's, also the lookups should not require the user ID as it 
### Should only look for the logged in token
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
