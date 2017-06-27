from graphscale import check
from graphscale.grapple.graphql_impl import gen_create_pent_dynamic, gen_delete_pent_dynamic

from . import generated


class Root(generated.QueryGenerated, generated.MutationGenerated):
    def __init__(self, context):
        self.__context = context

    @property
    def context(self):
        return self.__context

    # async def gen_delete_todo_user(self, obj_id):
    #     check.uuid_param(obj_id, 'obj_id')
    #     return await gen_delete_pent_dynamic(self.context, 'TodoUser', obj_id)


class TodoUser(generated.TodoUserGenerated):
    pass


class TodoItem(generated.TodoItemGenerated):
    pass
