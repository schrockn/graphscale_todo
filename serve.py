from graphscale.sql import ConnectionInfo
from graphscale.server import run_graphql_endpoint
from graphscale_todo.pent import Root
from graphscale_todo.config import single_db_context, in_mem_context
from graphscale_todo.graphql_schema import graphql_schema


def get_conn_info() -> ConnectionInfo:
    return ConnectionInfo(
        host='localhost',
        user='magnus',
        password='magnus',
        db='graphscale-todo',
    )


USE_MAGNUS_DB = False


def serve() -> None:
    if USE_MAGNUS_DB:
        run_graphql_endpoint(Root(single_db_context(get_conn_info())), graphql_schema())
    else:
        run_graphql_endpoint(Root(in_mem_context()), graphql_schema())


if __name__ == '__main__':
    serve()
