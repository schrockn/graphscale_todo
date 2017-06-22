from graphscale.server import define_graphql_endpoint
from graphscale_todo.pent import Root
from graphscale_todo.config import in_mem_context, single_db_context
from graphscale_todo.graphql_schema import graphql_schema
from collections import namedtuple

import pymysql.cursors

ConnectionInfo = namedtuple('ConnectionInfo', 'host user password db charset cursorclass')


def get_conn_info():
    return ConnectionInfo(
        host='localhost',
        user='magnus',
        password='magnus',
        db='graphscale-todo',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )


def serve(context):
    app = define_graphql_endpoint(Root(context), graphql_schema())
    app.run(host='0.0.0.0', debug=True, port=8080)


if __name__ == '__main__':
    serve(single_db_context(get_conn_info()))
