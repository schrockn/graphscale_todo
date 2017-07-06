from uuid import UUID

import pytest

from context import graphscale_todo
from graphscale.pent import PentContext
from graphscale.test.utils import async_test_graphql
from graphscale_todo.client import create_todo_mem_client
from graphscale_todo.graphql_schema import graphql_schema
from graphscale_todo.pent import Root

pytestmark = pytest.mark.asyncio


async def gen_todo_query(query: str, context: PentContext, variable_values: dict=None) -> None:
    return await async_test_graphql(
        query, context, graphql_schema(), root_value=Root(context), variable_values=variable_values
    )


async def test_create_delete_todo_user() -> None:
    client = create_todo_mem_client()
    create_result = await client.gen_create_todo_user({'name': 'Test Name', 'username': 'testname'})
    todo_id = UUID(hex=create_result['id'])

    delete_result = await client.gen_delete_todo_user(todo_id)
    assert delete_result['deletedId'] == str(todo_id)

    get_result = await client.gen_todo_user(todo_id)
    assert not get_result


async def test_create_update_todo_user() -> None:
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


async def test_create_todo_user_graphql() -> None:
    client = create_todo_mem_client()
    create_result = await client.gen_create_todo_user({'name': 'Test Name', 'username': 'testname'})

    assert isinstance(UUID(hex=create_result['id']), UUID)
    assert create_result['name'] == 'Test Name'
    assert create_result['username'] == 'testname'

    get_result = await client.gen_todo_user(UUID(hex=create_result['id']))
    assert get_result['name'] == 'Test Name'
    assert get_result['username'] == 'testname'


def get_objs_by_id(objs: list) -> dict:
    uuids = [UUID(hex=obj['id']) for obj in objs]
    return dict(zip(uuids, objs))


async def test_all_todo_users_graphql() -> None:
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


async def test_create_user_list_graphql() -> None:
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


async def test_create_todo_item_graphql() -> None:
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

    create_item_result = await client.gen_create_todo_item(
        {
            'text': 'Item one',
            'todoListId': list_id,
            'todoItemStatus': 'OPEN'
        }
    )

    item_id = UUID(hex=create_item_result['id'])

    gen_result = await client.gen_todo_item(item_id)
    assert gen_result['id'] == str(item_id)
    assert gen_result['text'] == 'Item one'
    assert gen_result['todoList']['name'] == 'List one'
    assert gen_result['todoList']['owner']['name'] == 'User one'
