from graphql import GraphQLSchema
from . import generated


def graphql_schema():
    return GraphQLSchema(query=generated.GraphQLQuery, mutation=generated.GraphQLMutation)
