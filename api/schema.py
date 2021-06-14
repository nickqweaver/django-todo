import graphene
from graphene_django import DjangoObjectType
from todo.query import TodoQuery
from todo.mutation import TodoMutation
from user.mutation import UserMutation
from user.query import UserQuery


class Query(TodoQuery, UserQuery):
    pass


class Mutation(TodoMutation, UserMutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
