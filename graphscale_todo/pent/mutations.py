from graphscale import check
from graphscale.pent import PentMutationData, create_pent

from . import generated, pents


class CreateTodoUserData(PentMutationData):
    @property
    def name(self):
        return self._data['name']


class CreateTodoItemData(PentMutationData):
    @property
    def text(self):
        return self._data['text']
