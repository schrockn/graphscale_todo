from graphscale import check
from graphscale.pent import Pent, create_pent, delete_pent, update_pent

class TodoUserGenerated(Pent):
    @property
    def obj_id(self):
        return self._data['obj_id']

    @property
    def name(self):
        return self._data['name']

class TodoItemGenerated(Pent):
    @property
    def obj_id(self):
        return self._data['obj_id']

    @property
    def text(self):
        return self._data['text']

class QueryGenerated:
    async def gen_todo_user(self, obj_id):
        check.uuid_param(obj_id, 'obj_id')
        cls = self.context.cls_from_name('TodoUser')
        return await cls.gen(self.context, obj_id)

    async def gen_todo_item(self, obj_id):
        check.uuid_param(obj_id, 'obj_id')
        cls = self.context.cls_from_name('TodoItem')
        return await cls.gen(self.context, obj_id)


class MutationGenerated:
    pass

