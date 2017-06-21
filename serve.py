from graphscale.server import define_graphql_endpoint
from graphscale_todo.pent import Root
from graphscale_todo.config import in_mem_context
from graphscale_todo.graphql_schema import graphql_schema


def serve(context):
    app = define_graphql_endpoint(Root(context), graphql_schema())
    app.run(host='0.0.0.0', debug=True, port=8080)


if __name__ == '__main__':
    serve(in_mem_context())
