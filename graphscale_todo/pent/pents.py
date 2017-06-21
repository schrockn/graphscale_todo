from graphscale import check
from graphscale.pent import create_pent

from . import generated
from .mutations import CreateTodoItemInput, CreateTodoUserInput


class Root(generated.QueryGenerated, generated.MutationGenerated):
    def __init__(self, context):
        self.context = context

    async def todo_user(self, obj_id):
        check.uuid_param(obj_id, 'obj_id')
        return await TodoUser.gen(self.context, obj_id)

    async def todo_item(self, obj_id):
        check.uuid_param(obj_id, 'obj_id')
        return await TodoItem.gen(self.context, obj_id)

    async def create_todo_user(self, input_obj):
        check.dict_param(input_obj, 'input_obj')
        return await create_pent(self.context, TodoUser, CreateTodoUserInput(input_obj))

    async def create_todo_item(self, input_obj):
        check.dict_param(input_obj, 'input_obj')
        return await create_pent(self.context, TodoItem, CreateTodoItemInput(input_obj))


class TodoUser(generated.TodoUserGenerated):
    pass


class TodoItem(generated.TodoItemGenerated):
    pass
