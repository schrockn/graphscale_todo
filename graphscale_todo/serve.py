from flask import Flask
from flask_graphql import GraphQLView
from graphscale import check
from graphscale.pent import PentContext, PentLoader
from graphscale_todo.pent import in_mem_context, Query
from graphscale_todo.graphql_schema import schema


def serve(context):
    check.param(context, PentContext, 'context')

    def produce_context():
        PentLoader.clear_instance()
        return context

    app = Flask(__name__)
    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema(),
            graphiql=True,
            context_factory=produce_context,
            root_value=Query(context),
        ),
    )

    app.run(host='0.0.0.0', debug=True, port=8080)


if __name__ == '__main__':
    serve(in_mem_context())
