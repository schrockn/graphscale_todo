from graphscale import check
from graphscale.pent import PentMutationData, create_pent, PentMutationPayload

from . import generated, pents
from collections import namedtuple


class CreateTodoUserData(generated.CreateTodoUserDataGenerated):
    pass


class UpdateTodoUserData(generated.UpdateTodoUserDataGenerated):
    pass


class CreateTodoItemData(generated.CreateTodoItemDataGenerated):
    pass


class CreateTodoListData(generated.CreateTodoListDataGenerated):
    pass


__CreateTodoUserPayloadDataMixin = namedtuple('__CreateTodoUserPayloadDataMixin', 'todo_user')


class CreateTodoUserPayload(PentMutationPayload, __CreateTodoUserPayloadDataMixin):
    pass


__CreateTodoListPayloadDataMixin = namedtuple('__CreateTodoListPayloadDataMixin', 'todo_list')


class CreateTodoListPayload(PentMutationPayload, __CreateTodoListPayloadDataMixin):
    pass


__CreateTodoItemPayloadDataMixin = namedtuple('__CreateTodoItemPayloadDataMixin', 'todo_item')


class CreateTodoItemPayload(PentMutationPayload, __CreateTodoItemPayloadDataMixin):
    pass


__UpdateTodoUserPayloadDataMixin = namedtuple('__UpdateTodoUserPayloadDataMixin', 'todo_user')


class UpdateTodoUserPayload(PentMutationPayload, __UpdateTodoUserPayloadDataMixin):
    pass
