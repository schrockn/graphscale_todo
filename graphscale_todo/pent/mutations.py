from graphscale import check
from . import generated

from graphscale.pent import create_pent, PentInput
from . import pents


class Mutation(generated.MutationGenerated):
    def __init__(self, context):
        self.context = context

    async def create_todo_user(self, input_object):
        check.param(input_object, CreateTodoUserInput, 'input_object')
        return await create_pent(self.context, pents.TodoUser, input_object)

    async def create_todo_item(self, input_object):
        check.param(input_object, CreateTodoItemInput, 'input_object')
        return await create_pent(self.context, pents.TodoItem, input_object)


class CreateTodoUserInput(PentInput):
    def __init__(self, data):
        super().__init__(data)


class CreateTodoItemInput(PentInput):
    def __init__(self, data):
        super().__init__(data)
