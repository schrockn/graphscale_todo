#W0611: unused imports lint
#C0301: line too long
#W0613: unused args because of locals hack
#pylint: disable=W0611, C0301, W0613

from collections import namedtuple
from enum import Enum, auto
from typing import List, Any
from uuid import UUID

from graphscale import check
from graphscale.grapple.graphql_impl import (
    gen_create_pent_dynamic,
    gen_delete_pent_dynamic,
    gen_update_pent_dynamic,
    gen_browse_pents_dynamic,
    gen_pent_dynamic,
    typed_or_none,
)
from graphscale.pent import (
    Pent,
    PentMutationData,
    PentMutationPayload,
    create_pent,
    delete_pent,
    update_pent,
    PentContextfulObject,
)


class TodoItemStatus(Enum):
    OPEN = 'OPEN'
    COMPLETED = 'COMPLETED'

class CreateTodoUserData(PentMutationData):
    def __init__(self, *,
        name: str,
        username: str,
    ) -> None:
        data = locals()
        del data['self']
        super().__init__(data)

    @property
    def name(self) -> str:
        return typed_or_none(self._data['name'], str) # type: ignore

    @property
    def username(self) -> str:
        return typed_or_none(self._data['username'], str) # type: ignore

class UpdateTodoUserData(PentMutationData):
    def __init__(self, *,
        name: str=None,
    ) -> None:
        data = locals()
        del data['self']
        super().__init__(data)

    @property
    def name(self) -> str:
        return typed_or_none(self._data.get('name'), str) # type: ignore

class CreateTodoListData(PentMutationData):
    def __init__(self, *,
        name: str,
        owner_id: UUID,
    ) -> None:
        data = locals()
        del data['self']
        super().__init__(data)

    @property
    def name(self) -> str:
        return typed_or_none(self._data['name'], str) # type: ignore

    @property
    def owner_id(self) -> UUID:
        return typed_or_none(self._data['owner_id'], UUID) # type: ignore

class CreateTodoItemData(PentMutationData):
    def __init__(self, *,
        text: str,
        todo_list_id: UUID,
        todo_item_status: TodoItemStatus,
    ) -> None:
        data = locals()
        del data['self']
        super().__init__(data)

    @property
    def text(self) -> str:
        return typed_or_none(self._data['text'], str) # type: ignore

    @property
    def todo_list_id(self) -> UUID:
        return typed_or_none(self._data['todo_list_id'], UUID) # type: ignore

    @property
    def todo_item_status(self) -> Any: # mypy circ: TodoItemStatus
        return self._data['todo_item_status'] # type: ignore


__CreateTodoUserPayloadDataMixin = namedtuple('__CreateTodoUserPayloadDataMixin', 'todo_user')


class CreateTodoUserPayload(PentMutationPayload, __CreateTodoUserPayloadDataMixin):
    pass


__UpdateTodoUserPayloadDataMixin = namedtuple('__UpdateTodoUserPayloadDataMixin', 'todo_user')


class UpdateTodoUserPayload(PentMutationPayload, __UpdateTodoUserPayloadDataMixin):
    pass


__DeleteTodoUserPayloadDataMixin = namedtuple('__DeleteTodoUserPayloadDataMixin', 'deleted_id')


class DeleteTodoUserPayload(PentMutationPayload, __DeleteTodoUserPayloadDataMixin):
    pass


__CreateTodoListPayloadDataMixin = namedtuple('__CreateTodoListPayloadDataMixin', 'todo_list')


class CreateTodoListPayload(PentMutationPayload, __CreateTodoListPayloadDataMixin):
    pass


__CreateTodoItemPayloadDataMixin = namedtuple('__CreateTodoItemPayloadDataMixin', 'todo_item')


class CreateTodoItemPayload(PentMutationPayload, __CreateTodoItemPayloadDataMixin):
    pass


__DeleteTodoItemPayloadDataMixin = namedtuple('__DeleteTodoItemPayloadDataMixin', 'deleted_id')


class DeleteTodoItemPayload(PentMutationPayload, __DeleteTodoItemPayloadDataMixin):
    pass

__all__ = [
    'CreateTodoUserData',
    'UpdateTodoUserData',
    'CreateTodoListData',
    'CreateTodoItemData',
    'CreateTodoUserPayload',
    'UpdateTodoUserPayload',
    'DeleteTodoUserPayload',
    'CreateTodoListPayload',
    'CreateTodoItemPayload',
    'DeleteTodoItemPayload',
    'TodoItemStatus',
]
