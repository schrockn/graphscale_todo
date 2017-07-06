from graphql import GraphQLSchema
from . import generated


def graphql_schema() -> GraphQLSchema:
    mutation = generated.GraphQLMutation if hasattr(generated, 'GraphQLMutation') else None
    return GraphQLSchema(query=generated.GraphQLQuery, mutation=mutation)
