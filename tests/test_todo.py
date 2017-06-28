from uuid import UUID

import pytest

from context import graphscale_todo
from graphscale import check
from graphscale.graphql_client import GraphQLArg, InProcessGraphQLClient
from graphscale.test.utils import async_test_graphql
from graphscale_todo.config import in_mem_context
from graphscale_todo.graphql_schema import graphql_schema
from graphscale_todo.pent import (CreateTodoItemData, CreateTodoUserData, Root, TodoItem, TodoUser)

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
            'createTodoUser(data: $data) { todoUser { id name username } }',
            GraphQLArg(name='data', arg_type='CreateTodoUserData!', value=data)
        )
        return result['createTodoUser']['todoUser']

    async def gen_delete_todo_user(self, obj_id):
        check.uuid_param(obj_id, 'obj_id')
        result = await self.graphql_client.gen_mutation(
            'deleteTodoUser(id: $id) { id name username }',
            GraphQLArg(name='id', arg_type='UUID!', value=obj_id)
        )
        return result['deleteTodoUser']

    async def gen_update_todo_user(self, obj_id, data):
        check.uuid_param(obj_id, 'obj_id')
        check.dict_param(data, 'data')
        result = await self.graphql_client.gen_mutation(
            'updateTodoUser(id: $id, data: $data) { todoUser { id name username } }',
            GraphQLArg(name='id', arg_type='UUID!', value=obj_id),
            GraphQLArg(name='data', arg_type='UpdateTodoUserData!', value=data)
        )
        return result['updateTodoUser']['todoUser']

    async def gen_create_todo_list(self, data):
        check.dict_param(data, 'data')
        result = await self.graphql_client.gen_mutation(
            'createTodoList(data: $data) { todoList { id name } } ',
            GraphQLArg(name='data', arg_type='CreateTodoListData!', value=data)
        )
        return result['createTodoList']['todoList']

    async def gen_todo_list(self, obj_id):
        check.uuid_param(obj_id, 'obj_id')
        result = await self.graphql_client.gen_query(
            'todoList(id: $id) { id name owner { id name } }',
            GraphQLArg(name='id', arg_type='UUID!', value=obj_id),
        )
        return result['todoList']

    async def gen_create_todo_item(self, data):
        check.dict_param(data, 'data')
        result = await self.graphql_client.gen_mutation(
            'createTodoItem(data: $data) { todoItem { id text } }',
            GraphQLArg(name='data', arg_type='CreateTodoItemData!', value=data)
        )
        return result['createTodoItem']['todoItem']

    async def gen_todo_user(self, obj_id):
        check.uuid_param(obj_id, 'obj_id')
        result = await self.graphql_client.gen_query(
            'todoUser(id: $id) { id name username }',
            GraphQLArg(name='id', arg_type='UUID!', value=obj_id)
        )
        return result['todoUser']

    async def gen_todo_user_complete_graph(self, obj_id):
        check.uuid_param(obj_id, 'obj_id')
        result = await self.graphql_client.gen_query(
            'todoUser(id: $id) { id name username todoLists { id name } }',
            GraphQLArg(name='id', arg_type='UUID!', value=obj_id)
        )
        return result['todoUser']

    async def gen_all_todo_users(self, first=100, after=None):
        check.int_param(first, 'first')
        check.opt_uuid_param(after, 'after')
        result = await self.graphql_client.gen_query(
            'allTodoUsers(after: $after, first: $first) { id name username }',
            GraphQLArg(name='after', arg_type='UUID', value=after),
            GraphQLArg(name='first', arg_type='Int', value=first)
        )
        return result['allTodoUsers']

    async def gen_todo_item(self, obj_id):
        check.uuid_param(obj_id, 'obj_id')
        result = await self.graphql_client.gen_query(
            """
            todoItem(id: $id) {
                id
                text
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
        return result['todoItem']


def create_todo_mem_client():
    return TodoGraphQLClient(InProcessGraphQLClient(Root(in_mem_context()), graphql_schema()))


async def test_create_delete_todo_user():
    client = create_todo_mem_client()
    create_result = await client.gen_create_todo_user({'name': 'Test Name', 'username': 'testname'})
    todo_id = UUID(hex=create_result['id'])

    delete_result = await client.gen_delete_todo_user(todo_id)
    assert delete_result['id'] == str(todo_id)

    get_result = await client.gen_todo_user(todo_id)
    assert not get_result


async def test_create_update_todo_user():
    client = create_todo_mem_client()
    create_result = await client.gen_create_todo_user({'name': 'Test Name', 'username': 'testname'})
    todo_id = UUID(hex=create_result['id'])

    update_result = await client.gen_update_todo_user(todo_id, {'name': 'New Name'})
    assert update_result['id'] == str(todo_id)
    assert update_result['name'] == 'New Name'
    assert update_result['username'] == 'testname'

    get_result = await client.gen_todo_user(todo_id)
    assert get_result['id'] == str(todo_id)
    assert get_result['name'] == 'New Name'
    assert get_result['username'] == 'testname'


async def test_create_todo_user_graphql():
    client = create_todo_mem_client()
    create_result = await client.gen_create_todo_user({'name': 'Test Name', 'username': 'testname'})

    assert isinstance(UUID(hex=create_result['id']), UUID)
    assert create_result['name'] == 'Test Name'
    assert create_result['username'] == 'testname'

    get_result = await client.gen_todo_user(UUID(hex=create_result['id']))
    assert get_result['name'] == 'Test Name'
    assert get_result['username'] == 'testname'


def get_objs_by_id(objs):
    uuids = [UUID(hex=obj['id']) for obj in objs]
    return dict(zip(uuids, objs))


async def test_all_todo_users_graphql():
    client = create_todo_mem_client()
    create_result_one = await client.gen_create_todo_user(
        {
            'name': 'User One',
            'username': 'userone'
        }
    )
    id_one = UUID(hex=create_result_one['id'])
    create_result_two = await client.gen_create_todo_user(
        {
            'name': 'User Two',
            'username': 'usertwo'
        }
    )
    id_two = UUID(hex=create_result_two['id'])
    create_result_three = await client.gen_create_todo_user(
        {
            'name': 'User Three',
            'username': 'userthree'
        }
    )
    id_three = UUID(hex=create_result_three['id'])

    low_id, mid_id, high_id = tuple(sorted([id_one, id_two, id_three]))

    after_low_id_objs = await client.gen_all_todo_users(after=low_id)
    assert len(after_low_id_objs) == 2

    obj_by_id = get_objs_by_id(after_low_id_objs)
    assert list(obj_by_id.keys()) == [mid_id, high_id]

    if id_one in obj_by_id:
        assert obj_by_id[id_one]['name'] == 'User One'

    if id_two in obj_by_id:
        assert obj_by_id[id_two]['name'] == 'User Two'

    if id_three in obj_by_id:
        assert obj_by_id[id_three]['name'] == 'User Three'

    after_low_first_one_objs = await client.gen_all_todo_users(after=low_id, first=1)
    assert len(after_low_first_one_objs) == 1
    assert list(get_objs_by_id(after_low_first_one_objs).keys())[0] == mid_id


async def test_create_user_list_graphql():
    client = create_todo_mem_client()
    create_user_result = await client.gen_create_todo_user(
        {
            'name': 'User With Two Lists',
            'username': 'usertwolists'
        }
    )

    user_id = UUID(hex=create_user_result['id'])

    create_list_one_result = await client.gen_create_todo_list(
        {
            'name': 'List One',
            'ownerId': user_id
        }
    )
    list_one_id = UUID(hex=create_list_one_result['id'])
    assert create_list_one_result['name'] == 'List One'

    get_list_one_result = await client.gen_todo_list(list_one_id)
    assert get_list_one_result['id'] == str(list_one_id)
    assert get_list_one_result['name'] == 'List One'
    assert get_list_one_result['owner']['id'] == str(user_id)
    assert get_list_one_result['owner']['name'] == 'User With Two Lists'

    create_list_result = await client.gen_create_todo_list({'name': 'List Two', 'ownerId': user_id})
    list_two_id = UUID(hex=create_list_result['id'])

    get_list_two_result = await client.gen_todo_list(list_two_id)
    assert get_list_two_result['id'] == str(list_two_id)
    assert get_list_two_result['name'] == 'List Two'
    assert get_list_two_result['owner']['id'] == str(user_id)
    assert get_list_two_result['owner']['name'] == 'User With Two Lists'

    user_graph = await client.gen_todo_user_complete_graph(user_id)
    assert user_graph['id'] == str(user_id)
    assert user_graph['name'] == 'User With Two Lists'
    assert len(user_graph['todoLists']) == 2
    todo_lists = get_objs_by_id(user_graph['todoLists'])
    assert todo_lists[list_one_id]['name'] == 'List One'
    assert todo_lists[list_two_id]['name'] == 'List Two'


async def test_create_todo_item_graphql():
    client = create_todo_mem_client()
    create_user_result = await client.gen_create_todo_user(
        {
            'name': 'User one',
            'username': 'test_create_todo_item_graphql_user'
        }
    )

    user_id = UUID(hex=create_user_result['id'])

    create_list_result = await client.gen_create_todo_list({'name': 'List one', 'ownerId': user_id})

    list_id = UUID(hex=create_list_result['id'])

    create_item_result = await client.gen_create_todo_item({'text': 'Item one', 'listId': list_id})

    item_id = UUID(hex=create_item_result['id'])

    gen_result = await client.gen_todo_item(item_id)
    assert gen_result['id'] == str(item_id)
    assert gen_result['text'] == 'Item one'
    assert gen_result['list']['name'] == 'List one'
    assert gen_result['list']['owner']['name'] == 'User one'
