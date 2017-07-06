from typing import Any, Dict, cast
from uuid import UUID

from graphscale.graphql_client import GraphQLArg, InProcessGraphQLClient
from .pent import Root
from .config import in_mem_context
from .graphql_schema import graphql_schema

Bag = Dict[str, Any]


class TodoGraphQLClient:
    def __init__(self, graphql_client: InProcessGraphQLClient) -> None:
        self.graphql_client = graphql_client

    async def gen_create_todo_user(self, data: Bag) -> Bag:
        result = await self.graphql_client.gen_mutation(
            'createTodoUser(data: $data) { todoUser { id name username } }',
            GraphQLArg(name='data', arg_type='CreateTodoUserData!', value=data)
        )
        return cast(Bag, result['createTodoUser']['todoUser'])

    async def gen_delete_todo_user(self, obj_id: UUID) -> Bag:
        result = await self.graphql_client.gen_mutation(
            'deleteTodoUser(id: $id) { deletedId }',
            GraphQLArg(name='id', arg_type='UUID!', value=obj_id)
        )
        return cast(Bag, result['deleteTodoUser'])

    async def gen_update_todo_user(self, obj_id: UUID, data: Bag) -> Bag:
        result = await self.graphql_client.gen_mutation(
            'updateTodoUser(id: $id, data: $data) { todoUser { id name username } }',
            GraphQLArg(name='id', arg_type='UUID!', value=obj_id),
            GraphQLArg(name='data', arg_type='UpdateTodoUserData!', value=data)
        )
        return cast(Bag, result['updateTodoUser']['todoUser'])

    async def gen_create_todo_list(self, data: Bag) -> Bag:
        result = await self.graphql_client.gen_mutation(
            'createTodoList(data: $data) { todoList { id name } } ',
            GraphQLArg(name='data', arg_type='CreateTodoListData!', value=data)
        )
        return cast(Bag, result['createTodoList']['todoList'])

    async def gen_todo_list(self, obj_id: UUID) -> Bag:
        result = await self.graphql_client.gen_query(
            'todoList(id: $id) { id name owner { id name } }',
            GraphQLArg(name='id', arg_type='UUID!', value=obj_id),
        )
        return cast(Bag, result['todoList'])

    async def gen_create_todo_item(self, data: Bag) -> Bag:
        result = await self.graphql_client.gen_mutation(
            'createTodoItem(data: $data) { todoItem { id text todoItemStatus } }',
            GraphQLArg(name='data', arg_type='CreateTodoItemData!', value=data)
        )
        return cast(Bag, result['createTodoItem']['todoItem'])

    async def gen_todo_user(self, obj_id: UUID) -> Bag:
        result = await self.graphql_client.gen_query(
            'todoUser(id: $id) { id name username }',
            GraphQLArg(name='id', arg_type='UUID!', value=obj_id)
        )
        return cast(Bag, result['todoUser'])

    async def gen_todo_user_complete_graph(self, obj_id: UUID) -> Bag:
        result = await self.graphql_client.gen_query(
            'todoUser(id: $id) { id name username todoLists { id name } }',
            GraphQLArg(name='id', arg_type='UUID!', value=obj_id)
        )
        return cast(Bag, result['todoUser'])

    async def gen_all_todo_users(self, first: int=100, after: UUID=None) -> Bag:
        result = await self.graphql_client.gen_query(
            'allTodoUsers(after: $after, first: $first) { id name username }',
            GraphQLArg(name='after', arg_type='UUID', value=after),
            GraphQLArg(name='first', arg_type='Int', value=first)
        )
        return cast(Bag, result['allTodoUsers'])

    async def gen_todo_item(self, obj_id: UUID) -> Bag:
        result = await self.graphql_client.gen_query(
            """
            todoItem(id: $id) {
                id
                text
                todoItemStatus
                list {
                    id
                    name
                    owner {
                        id
                        name
                    }
                }
            }""", GraphQLArg(name='id', arg_type='UUID!', value=obj_id)
        )
        return cast(Bag, result['todoItem'])


def create_todo_mem_client() -> TodoGraphQLClient:
    return TodoGraphQLClient(InProcessGraphQLClient(Root(in_mem_context()), graphql_schema()))
