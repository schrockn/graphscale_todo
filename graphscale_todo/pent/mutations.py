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


class CreateTodoUserPayload(PentMutationPayload, generated.CreateTodoUserPayloadDataMixin):
    pass


class CreateTodoListPayload(PentMutationPayload, generated.CreateTodoListPayloadDataMixin):
    pass


class CreateTodoItemPayload(PentMutationPayload, generated.CreateTodoItemPayloadDataMixin):
    pass


class UpdateTodoUserPayload(PentMutationPayload, generated.UpdateTodoUserPayloadDataMixin):
    pass


class DeleteTodoUserPayload(PentMutationPayload, generated.DeleteTodoUserPayloadDataMixin):
    pass


class DeleteTodoItemPayload(PentMutationPayload, generated.DeleteTodoItemPayloadDataMixin):
    pass
