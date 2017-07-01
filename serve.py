from graphscale.sql import create_conn_info
from graphscale.server import run_graphql_endpoint
from graphscale_todo.pent import Root
from graphscale_todo.config import single_db_context
from graphscale_todo.graphql_schema import graphql_schema


def get_conn_info():
    return create_conn_info(
        host='localhost',
        user='magnus',
        password='magnus',
        db='graphscale-todo',
    )


def serve(context):
    run_graphql_endpoint(Root(context), graphql_schema())


if __name__ == '__main__':
    serve(single_db_context(get_conn_info()))
