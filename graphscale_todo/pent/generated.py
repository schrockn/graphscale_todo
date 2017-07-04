#W0611: unused imports lint
#C0301: line too long
#W0613: unused args because of locals hack
#pylint: disable=W0611, C0301, W0613

from collections import namedtuple
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

from . import pents

class QueryGenerated(PentContextfulObject):
    async def gen_todo_user(self, obj_id: UUID) -> Pent:
        return await gen_pent_dynamic(self.context, 'TodoUser', obj_id)

    async def gen_all_todo_users(self, first: int, after: UUID=None) -> List[Pent]:
        return await gen_browse_pents_dynamic(self.context, after, first, 'TodoUser') # type: ignore

    async def gen_todo_item(self, obj_id: UUID) -> Pent:
        return await gen_pent_dynamic(self.context, 'TodoItem', obj_id)

    async def gen_all_todo_items(self, first: int, after: UUID=None) -> List[Pent]:
        return await gen_browse_pents_dynamic(self.context, after, first, 'TodoItem') # type: ignore

    async def gen_todo_list(self, obj_id: UUID) -> Pent:
        return await gen_pent_dynamic(self.context, 'TodoList', obj_id)


class MutationGenerated(PentContextfulObject):
    async def gen_create_todo_user(self, data: PentMutationData) -> PentMutationPayload:
        return await gen_create_pent_dynamic(self.context, 'TodoUser', 'CreateTodoUserData', 'CreateTodoUserPayload', data)

    async def gen_update_todo_user(self, obj_id: UUID, data: PentMutationData) -> PentMutationPayload:
        return await gen_update_pent_dynamic(self.context, obj_id, 'TodoUser', 'UpdateTodoUserData', 'UpdateTodoUserPayload', data)

    async def gen_delete_todo_user(self, obj_id: UUID) -> PentMutationPayload:
        return await gen_delete_pent_dynamic(self.context, 'TodoUser', 'DeleteTodoUserPayload', obj_id)

    async def gen_create_todo_list(self, data: PentMutationData) -> PentMutationPayload:
        return await gen_create_pent_dynamic(self.context, 'TodoList', 'CreateTodoListData', 'CreateTodoListPayload', data)

    async def gen_create_todo_item(self, data: PentMutationData) -> PentMutationPayload:
        return await gen_create_pent_dynamic(self.context, 'TodoItem', 'CreateTodoItemData', 'CreateTodoItemPayload', data)

    async def gen_delete_todo_item(self, obj_id: UUID) -> PentMutationPayload:
        return await gen_delete_pent_dynamic(self.context, 'TodoItem', 'DeleteTodoItemPayload', obj_id)


class TodoUserGenerated(Pent):
    @property
    def obj_id(self) -> UUID:
        return self._data['obj_id'] # type: ignore

    @property
    def name(self) -> str:
        return self._data['name'] # type: ignore

    @property
    def username(self) -> str:
        return self._data['username'] # type: ignore

    async def gen_todo_lists(self, first: int, after: UUID=None) -> List[Pent]:
        return await self.gen_associated_pents_dynamic('TodoList', 'user_to_list_edge', after, first) # type: ignore

class TodoListGenerated(Pent):
    @property
    def obj_id(self) -> UUID:
        return self._data['obj_id'] # type: ignore

    @property
    def name(self) -> str:
        return self._data['name'] # type: ignore

    async def gen_owner(self) -> Pent:
        return await self.gen_from_stored_id_dynamic('TodoUser', 'owner_id')

    async def gen_todo_items(self, first: int, after: UUID=None) -> List[Pent]:
        return await self.gen_associated_pents_dynamic('TodoItem', 'list_to_item_edge', after, first) # type: ignore

class TodoItemGenerated(Pent):
    @property
    def obj_id(self) -> UUID:
        return self._data['obj_id'] # type: ignore

    @property
    def text(self) -> str:
        return self._data['text'] # type: ignore

    async def gen_list(self) -> Pent:
        return await self.gen_from_stored_id_dynamic('TodoList', 'list_id')

class CreateTodoUserDataGenerated(PentMutationData):
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

class UpdateTodoUserDataGenerated(PentMutationData):
    def __init__(self, *,
        name: str=None,
    ) -> None:
        data = locals()
        del data['self']
        super().__init__(data)

    @property
    def name(self) -> str:
        return self._data.get('name') # type: ignore

class CreateTodoListDataGenerated(PentMutationData):
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

class CreateTodoItemDataGenerated(PentMutationData):
    def __init__(self, *,
        text: str,
        list_id: UUID,
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



CreateTodoUserPayloadDataMixin = namedtuple('CreateTodoUserPayloadDataMixin', 'todo_user')


UpdateTodoUserPayloadDataMixin = namedtuple('UpdateTodoUserPayloadDataMixin', 'todo_user')


DeleteTodoUserPayloadDataMixin = namedtuple('DeleteTodoUserPayloadDataMixin', 'deleted_id')


CreateTodoListPayloadDataMixin = namedtuple('CreateTodoListPayloadDataMixin', 'todo_list')


CreateTodoItemPayloadDataMixin = namedtuple('CreateTodoItemPayloadDataMixin', 'todo_item')


DeleteTodoItemPayloadDataMixin = namedtuple('DeleteTodoItemPayloadDataMixin', 'deleted_id')
