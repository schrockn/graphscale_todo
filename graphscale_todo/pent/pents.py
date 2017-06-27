from graphscale import check
from graphscale.grapple.graphql_impl import gen_browse_pents_dynamic
# from graphscale.pent import update_pent

from . import generated


class Root(generated.QueryGenerated, generated.MutationGenerated):
    def __init__(self, context):
        self.__context = context

    @property
    def context(self):
        return self.__context


class TodoUser(generated.TodoUserGenerated):
    pass


class TodoItem(generated.TodoItemGenerated):
    pass


class TodoList(generated.TodoListGenerated):
    pass
