from graphscale import check
from . import generated

from graphscale.pent import create_pent, PentInput
from . import pents


class CreateTodoUserInput(PentInput):
    def __init__(self, data):
        super().__init__(data)


class CreateTodoItemInput(PentInput):
    def __init__(self, data):
        super().__init__(data)
