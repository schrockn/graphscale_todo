from graphql import GraphQLSchema
from . import generated


def graphql_schema() -> GraphQLSchema:
    return GraphQLSchema(query=generated.GraphQLQuery, mutation=generated.GraphQLMutation)
