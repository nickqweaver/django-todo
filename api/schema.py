import graphene
from graphene_django import DjangoObjectType
from todo.query import TodoQuery
from todo.mutation import TodoMutation


class Query(TodoQuery):
    pass


class Mutation(TodoMutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
