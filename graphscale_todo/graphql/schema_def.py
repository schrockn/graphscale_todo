from graphql import GraphQLSchema

from . import types

def create_schema():
    return GraphQLSchema(query=types.GraphQLQuery, mutation=types.GraphQLMutation)
