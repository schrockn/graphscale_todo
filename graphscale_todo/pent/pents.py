from . import generated

# from graphscale.pent import delete_pent
# from graphscale.grapple.graphql_impl import gen_delete_pent_dynamic

# from .mutations import DeleteTodoUserPayload


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
