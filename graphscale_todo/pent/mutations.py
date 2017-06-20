from graphscale import check
from . import generated

from graphscale.pent import create_pent, PentInput
from . import pents


class CreateTodoUserInput(PentInput):
    def __init__(self, data):
        check.param_invariant(isinstance(data['name'], str), 'data')
        self.data = data


class Mutation(generated.MutationGenerated):
    def __init__(self, context):
        self.context = context

    async def create_source(self, input_object):
        check.param(input_object, CreateTodoUserInput, 'input_object')
        return await create_pent(self.context, pents.TodoUser, input_object)
