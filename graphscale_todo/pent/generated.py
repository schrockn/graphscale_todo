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


class RootGenerated(PentContextfulObject):
    async def gen_todo_user(self, obj_id: UUID) -> Pent: # mypy circ TodoUser
        return await gen_pent_dynamic(self.context, 'TodoUser', obj_id) # type: ignore

    async def gen_all_todo_users(self, first: int, after: UUID=None) -> List[Pent]: # mypy circ List[TodoUser]
        return await gen_browse_pents_dynamic(self.context, after, first, 'TodoUser') # type: ignore

    async def gen_todo_item(self, obj_id: UUID) -> Pent: # mypy circ TodoItem
        return await gen_pent_dynamic(self.context, 'TodoItem', obj_id) # type: ignore

    async def gen_all_todo_items(self, first: int, after: UUID=None) -> List[Pent]: # mypy circ List[TodoItem]
        return await gen_browse_pents_dynamic(self.context, after, first, 'TodoItem') # type: ignore

    async def gen_todo_list(self, obj_id: UUID) -> Pent: # mypy circ TodoList
        return await gen_pent_dynamic(self.context, 'TodoList', obj_id) # type: ignore

    async def gen_create_todo_user(self, data: 'CreateTodoUserData') -> Pent: # mypy circ CreateTodoUserPayload
        return await gen_create_pent_dynamic(self.context, 'TodoUser', 'CreateTodoUserData', 'CreateTodoUserPayload', data) # type: ignore

    async def gen_update_todo_user(self, obj_id: UUID, data: 'UpdateTodoUserData') -> PentMutationPayload: # mypy circ UpdateTodoUserPayload
        return await gen_update_pent_dynamic(self.context, obj_id, 'TodoUser', 'UpdateTodoUserData', 'UpdateTodoUserPayload', data) # type: ignore

    async def gen_delete_todo_user(self, obj_id: UUID) -> PentMutationPayload: # mypy circ DeleteTodoUserPayload
        return await gen_delete_pent_dynamic(self.context, 'TodoUser', 'DeleteTodoUserPayload', obj_id) # type: ignore

    async def gen_create_todo_list(self, data: 'CreateTodoListData') -> Pent: # mypy circ CreateTodoListPayload
        return await gen_create_pent_dynamic(self.context, 'TodoList', 'CreateTodoListData', 'CreateTodoListPayload', data) # type: ignore

    async def gen_create_todo_item(self, data: 'CreateTodoItemData') -> Pent: # mypy circ CreateTodoItemPayload
        return await gen_create_pent_dynamic(self.context, 'TodoItem', 'CreateTodoItemData', 'CreateTodoItemPayload', data) # type: ignore

    async def gen_delete_todo_item(self, obj_id: UUID) -> PentMutationPayload: # mypy circ DeleteTodoItemPayload
        return await gen_delete_pent_dynamic(self.context, 'TodoItem', 'DeleteTodoItemPayload', obj_id) # type: ignore


class TodoUserGenerated(Pent):
    @property
    def obj_id(self) -> UUID:
        return typed_or_none(self._data['obj_id'], UUID) # type: ignore

    @property
    def name(self) -> str:
        return typed_or_none(self._data['name'], str) # type: ignore

    @property
    def username(self) -> str:
        return typed_or_none(self._data['username'], str) # type: ignore

    async def gen_todo_lists(self, first: int, after: UUID=None) -> List[Pent]: # mypy circ 'List[TodoList]'
        return await self.gen_associated_pents_dynamic('TodoList', 'user_to_list_edge', after, first) # type: ignore

class TodoListGenerated(Pent):
    @property
    def obj_id(self) -> UUID:
        return typed_or_none(self._data['obj_id'], UUID) # type: ignore

    @property
    def name(self) -> str:
        return typed_or_none(self._data['name'], str) # type: ignore

    async def gen_owner(self) -> Pent: # mypy circ TodoUser
        return await self.gen_from_stored_id_dynamic('TodoUser', 'owner_id') # type: ignore

    async def gen_todo_items(self, first: int, after: UUID=None) -> List[Pent]: # mypy circ 'List[TodoItem]'
        return await self.gen_associated_pents_dynamic('TodoItem', 'list_to_item_edge', after, first) # type: ignore

class TodoItemGenerated(Pent):
    @property
    def obj_id(self) -> UUID:
        return typed_or_none(self._data['obj_id'], UUID) # type: ignore

    @property
    def text(self) -> str:
        return typed_or_none(self._data['text'], str) # type: ignore

    async def gen_todo_list(self) -> Pent: # mypy circ TodoList
        return await self.gen_from_stored_id_dynamic('TodoList', 'todo_list_id') # type: ignore

    @property
    def todo_item_status(self) -> Any: # mypy circ: TodoItemStatus
        return self._data['todo_item_status'] # type: ignore

