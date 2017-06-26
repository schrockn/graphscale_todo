from uuid import UUID

import pytest

from context import graphscale_todo
from graphscale import check
from graphscale.graphql_client import GraphQLArg, InProcessGraphQLClient
from graphscale.test.utils import async_test_graphql
from graphscale_todo.config import in_mem_context
from graphscale_todo.graphql_schema import graphql_schema
from graphscale_todo.pent import (
    CreateTodoItemInput, CreateTodoUserInput, Root, TodoItem, TodoUser
)

pytestmark = pytest.mark.asyncio


async def gen_todo_query(query, context, variable_values=None):
    return await async_test_graphql(
        query, context, graphql_schema(), root_value=Root(context), variable_values=variable_values
    )


class TodoGraphQLClient:
    def __init__(self, graphql_client):
        self.graphql_client = graphql_client

    async def gen_create_todo_user(self, data):
        check.dict_param(data, 'data')
        result = await self.graphql_client.gen_mutation(
            'createTodoUser(data: $data) { id name }',
            GraphQLArg(name='data', arg_type='CreateTodoUserInput!', value=data)
        )
        return result['createTodoUser']

    async def gen_create_todo_item(self, data):
        check.dict_param(data, 'data')
        result = await self.graphql_client.gen_mutation(
            'createTodoItem(data: $data) { id text}',
            GraphQLArg(name='data', arg_type='CreateTodoItemInput!', value=data)
        )
        return result['createTodoItem']

    async def gen_todo_user(self, obj_id):
        check.uuid_param(obj_id, 'obj_id')
        result = await self.graphql_client.gen_query(
            'todoUser(id: $id) { id name }', GraphQLArg(name='id', arg_type='UUID!', value=obj_id)
        )
        return result['todoUser']

    async def gen_todo_item(self, obj_id):
        check.uuid_param(obj_id, 'obj_id')
        result = await self.graphql_client.gen_query(
            'todoItem(id: $id) { id text }', GraphQLArg(name='id', arg_type='UUID!', value=obj_id)
        )
        return result['todoItem']


def create_todo_client():
    return TodoGraphQLClient(InProcessGraphQLClient(Root(in_mem_context()), graphql_schema()))


async def test_create_todo_user():
    context = in_mem_context()
    root = Root(context)
    dataect = {'name': 'Test Name'}
    out_todo = await root.gen_create_todo_user(dataect)
    assert isinstance(out_todo, TodoUser)
    assert out_todo.name == 'Test Name'

    todo = await root.gen_todo_user(out_todo.obj_id)
    assert isinstance(todo, TodoUser)
    assert todo.name == 'Test Name'


async def test_create_todo_user_graphql():
    client = create_todo_client()
    create_result = await client.gen_create_todo_user({'name': 'Test Name'})

    assert isinstance(UUID(hex=create_result['id']), UUID)
    assert create_result['name'] == 'Test Name'

    get_result = await client.gen_todo_user(UUID(hex=create_result['id']))
    assert get_result['name'] == 'Test Name'


async def test_create_todo_item_graphql():
    client = create_todo_client()
    create_result = await client.gen_create_todo_item({'text': 'Test Item'})
    new_id = UUID(hex=create_result['id'])
    assert create_result['text'] == 'Test Item'

    gen_result = await client.gen_todo_item(new_id)
    assert gen_result['id'] == str(new_id)
    assert gen_result['text'] == 'Test Item'


async def test_create_todo_item():
    context = in_mem_context()
    root = Root(context)
    dataect = {'text': 'Test Item'}
    out_todo_item = await root.create_todo_item(dataect)
    assert isinstance(out_todo_item, TodoItem)
    assert out_todo_item.text == 'Test Item'

    todo_item = await root.gen_todo_item(out_todo_item.obj_id)
    assert isinstance(todo_item, TodoItem)
    assert todo_item.text == 'Test Item'
