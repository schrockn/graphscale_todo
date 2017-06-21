from context import graphscale_todo
from graphscale_todo.pent import Root, CreateTodoUserInput, TodoUser
from graphscale_todo.config import in_mem_context
import pytest
pytestmark = pytest.mark.asyncio


async def test_test():
    context = in_mem_context()
    root = Root(context)
    input_object = {'name': 'Test Name'}
    out_todo = await root.create_todo_user(input_object)
    assert isinstance(out_todo, TodoUser)
    assert out_todo.name == 'Test Name'

    todo = await root.todo_user(out_todo.obj_id)
    assert isinstance(todo, TodoUser)
    assert todo.name == 'Test Name'
