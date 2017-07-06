from graphscale.pent import PentLoader
from graphscale.sql import ConnectionInfo
from graphscale.server import run_graphql_endpoint
from graphscale_todo.pent import Root
from graphscale_todo.config import single_db_context
from graphscale_todo.graphql_schema import graphql_schema


def get_conn_info() -> ConnectionInfo:
    return ConnectionInfo(
        host='localhost',
        user='magnus',
        password='magnus',
        db='graphscale-todo',
    )


def serve() -> None:
    run_graphql_endpoint(Root(single_db_context(get_conn_info())), graphql_schema())


if __name__ == '__main__':
    serve()
