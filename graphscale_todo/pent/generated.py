from graphscale import check
from graphscale.grapple.graphql_impl import (
    gen_create_pent_dynamic,
    gen_delete_pent_dynamic,
    gen_update_pent_dynamic,
    gen_browse_pents_dynamic,
)
from graphscale.pent import Pent, PentMutationData, create_pent, delete_pent, update_pent

class QueryGenerated:
    @property
    def context(self):
        raise Exception('must implement in Root')

    async def gen_todo_user(self, obj_id):
        check.uuid_param(obj_id, 'obj_id')
        cls = self.context.cls_from_name('TodoUser')
        return await cls.gen(self.context, obj_id)

    async def gen_all_todo_users(self, first, after=None):
        return await gen_browse_pents_dynamic(self.context, after, first, 'TodoUser')

    async def gen_todo_item(self, obj_id):
        check.uuid_param(obj_id, 'obj_id')
        cls = self.context.cls_from_name('TodoItem')
        return await cls.gen(self.context, obj_id)


class MutationGenerated:
    @property
    def context(self):
        raise Exception('must implement in Root')

    async def gen_create_todo_user(self, data):
        return await gen_create_pent_dynamic(self.context, 'TodoUser', 'CreateTodoUserData', data)

    async def gen_update_todo_user(self, obj_id, data):
        return await gen_update_pent_dynamic(self.context, obj_id, 'TodoUser', 'UpdateTodoUserData', data)

    async def gen_delete_todo_user(self, obj_id):
        return await gen_delete_pent_dynamic(self.context, 'TodoUser', obj_id)

    async def gen_create_todo_item(self, data):
        return await gen_create_pent_dynamic(self.context, 'TodoItem', 'CreateTodoItemData', data)

    async def gen_delete_todo_item(self, obj_id):
        return await gen_delete_pent_dynamic(self.context, 'TodoItem', obj_id)


class TodoUserGenerated(Pent):
    @property
    def obj_id(self):
        return self._data['obj_id']

    @property
    def name(self):
        return self._data['name']

    @property
    def username(self):
        return self._data['username']

class TodoItemGenerated(Pent):
    @property
    def obj_id(self):
        return self._data['obj_id']

    @property
    def text(self):
        return self._data['text']

class CreateTodoUserDataGenerated(PentMutationData):
    def __init__(self, *,
        name,
        username,
    ):
        self._data = locals()
        del self._data['self']

    @property
    def name(self):
        return self._data['name']

    @property
    def username(self):
        return self._data['username']

class UpdateTodoUserDataGenerated(PentMutationData):
    def __init__(self, *,
        name=None,
    ):
        self._data = locals()
        del self._data['self']

    @property
    def name(self):
        return self._data.get('name')

class CreateTodoItemDataGenerated(PentMutationData):
    def __init__(self, *,
        text,
    ):
        self._data = locals()
        del self._data['self']

    @property
    def text(self):
        return self._data['text']

