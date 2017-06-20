from graphscale import check
from . import generated


class Query(generated.QueryGenerated):
    def __init__(self, context):
        self.context = context

    async def todo_user(self, obj_id):
        check.uuid_param(obj_id, 'obj_id')
        return await TodoUser.gen(self.context, obj_id)

    async def todo_item(self, obj_id):
        check.uuid_param(obj_id, 'obj_id')
        return await TodoItem.gen(self.context, obj_id)


class TodoUser(generated.TodoUserGenerated):
    pass


class TodoItem(generated.TodoItem):
    pass
