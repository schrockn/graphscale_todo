from graphscale import check
from . import generated


class TodoUser(generated.TodoUserGenerated):
    pass


class Query(generated.QueryGenerated):
    def __init__(self, context):
        self.context = context

    async def todo_user(self, obj_id):
        check.uuid_param(obj_id, 'obj_id')
        return await TodoUser.gen(self.context, obj_id)


class TodoItem(generated.TodoItem):
    pass
