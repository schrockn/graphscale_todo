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
    async def gen_todo_lists(self, after=None, first=100):
        return await self.gen_associated_pents(TodoList, 'user_to_list_edge', after, first)


class TodoItem(generated.TodoItemGenerated):
    pass


class TodoList(generated.TodoListGenerated):
    pass
    # async def gen_owner(self):
    #     return await gen_from_stored_id_dynamic(self.context(), 'TodoUser', self._data, 'owner_id')
