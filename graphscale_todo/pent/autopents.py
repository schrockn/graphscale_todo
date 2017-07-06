#W0611: unused imports lint
#C0301: line too long
#W0613: unused args because of locals hack
#pylint: disable=W0611, C0301, W0613

from collections import namedtuple
from enum import Enum, auto
from typing import List
from uuid import UUID

from graphscale import check
from graphscale.grapple.graphql_impl import (
    gen_create_pent_dynamic,
    gen_delete_pent_dynamic,
    gen_update_pent_dynamic,
    gen_browse_pents_dynamic,
    gen_pent_dynamic,
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

class Root(PentContextfulObject):
    async def gen_todo_user(self, obj_id: UUID) -> 'TodoUser':
        return await gen_pent_dynamic(self.context, 'TodoUser', obj_id) # type: ignore

    async def gen_all_todo_users(self, first: int, after: UUID=None) -> 'List[TodoUser]':
        return await gen_browse_pents_dynamic(self.context, after, first, 'TodoUser') # type: ignore

    async def gen_todo_item(self, obj_id: UUID) -> 'TodoItem':
        return await gen_pent_dynamic(self.context, 'TodoItem', obj_id) # type: ignore

    async def gen_all_todo_items(self, first: int, after: UUID=None) -> 'List[TodoItem]':
        return await gen_browse_pents_dynamic(self.context, after, first, 'TodoItem') # type: ignore

    async def gen_todo_list(self, obj_id: UUID) -> 'TodoList':
        return await gen_pent_dynamic(self.context, 'TodoList', obj_id) # type: ignore

    async def gen_create_todo_user(self, data: 'CreateTodoUserData') -> 'CreateTodoUserPayload':
        return await gen_create_pent_dynamic(self.context, 'TodoUser', 'CreateTodoUserData', 'CreateTodoUserPayload', data) # type: ignore

    async def gen_update_todo_user(self, obj_id: UUID, data: 'UpdateTodoUserData') -> 'UpdateTodoUserPayload':
        return await gen_update_pent_dynamic(self.context, obj_id, 'TodoUser', 'UpdateTodoUserData', 'UpdateTodoUserPayload', data) # type: ignore

    async def gen_delete_todo_user(self, obj_id: UUID) -> 'DeleteTodoUserPayload':
        return await gen_delete_pent_dynamic(self.context, 'TodoUser', 'DeleteTodoUserPayload', obj_id) # type: ignore

    async def gen_create_todo_list(self, data: 'CreateTodoListData') -> 'CreateTodoListPayload':
        return await gen_create_pent_dynamic(self.context, 'TodoList', 'CreateTodoListData', 'CreateTodoListPayload', data) # type: ignore

    async def gen_create_todo_item(self, data: 'CreateTodoItemData') -> 'CreateTodoItemPayload':
        return await gen_create_pent_dynamic(self.context, 'TodoItem', 'CreateTodoItemData', 'CreateTodoItemPayload', data) # type: ignore

    async def gen_delete_todo_item(self, obj_id: UUID) -> 'DeleteTodoItemPayload':
        return await gen_delete_pent_dynamic(self.context, 'TodoItem', 'DeleteTodoItemPayload', obj_id) # type: ignore


class TodoUser(Pent):
    @property
    def obj_id(self) -> UUID:
        return self._data['obj_id'] # type: ignore

    @property
    def name(self) -> str:
        return self._data['name'] # type: ignore

    @property
    def username(self) -> str:
        return self._data['username'] # type: ignore

    async def gen_todo_lists(self, first: int, after: UUID=None) -> 'List[TodoList]':
        return await self.gen_associated_pents_dynamic('TodoList', 'user_to_list_edge', after, first) # type: ignore

class TodoList(Pent):
    @property
    def obj_id(self) -> UUID:
        return self._data['obj_id'] # type: ignore

    @property
    def name(self) -> str:
        return self._data['name'] # type: ignore

    async def gen_owner(self) -> 'TodoUser':
        return await self.gen_from_stored_id_dynamic('TodoUser', 'owner_id') # type: ignore

    async def gen_todo_items(self, first: int, after: UUID=None) -> 'List[TodoItem]':
        return await self.gen_associated_pents_dynamic('TodoItem', 'list_to_item_edge', after, first) # type: ignore

class TodoItem(Pent):
    @property
    def obj_id(self) -> UUID:
        return self._data['obj_id'] # type: ignore

    @property
    def text(self) -> str:
        return self._data['text'] # type: ignore

    async def gen_list(self) -> 'TodoList':
        return await self.gen_from_stored_id_dynamic('TodoList', 'list_id') # type: ignore

    @property
    def todo_item_status(self) -> TodoItemStatus:
        return self._data['todo_item_status'] # type: ignore

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
        return self._data['name'] # type: ignore

    @property
    def username(self) -> str:
        return self._data['username'] # type: ignore

class UpdateTodoUserData(PentMutationData):
    def __init__(self, *,
        name: str=None,
    ) -> None:
        data = locals()
        del data['self']
        super().__init__(data)

    @property
    def name(self) -> str:
        return self._data.get('name') # type: ignore

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
        return self._data['name'] # type: ignore

    @property
    def owner_id(self) -> UUID:
        return self._data['owner_id'] # type: ignore

class CreateTodoItemData(PentMutationData):
    def __init__(self, *,
        text: str,
        list_id: UUID,
        todo_item_status: TodoItemStatus,
    ) -> None:
        data = locals()
        del data['self']
        super().__init__(data)

    @property
    def text(self) -> str:
        return self._data['text'] # type: ignore

    @property
    def list_id(self) -> UUID:
        return self._data['list_id'] # type: ignore

    @property
    def todo_item_status(self) -> TodoItemStatus:
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
    'Root',
    'TodoUser',
    'TodoList',
    'TodoItem',
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
