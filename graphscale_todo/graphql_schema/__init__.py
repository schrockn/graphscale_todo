from graphql import GraphQLSchema
from . import types


def graphql_schema():
    return GraphQLSchema(query=types.GraphQLQuery, mutation=types.GraphQLMutation)
