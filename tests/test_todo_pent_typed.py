import pytest

from context import graphscale_todo
from graphscale_todo.pent.autopents import Root, CreateTodoUserData
from graphscale_todo.config import in_mem_context

pytestmark = pytest.mark.asyncio


async def test_gen_user() -> None:
    root = Root(in_mem_context())
    payload = await root.gen_create_todo_user(
        CreateTodoUserData(name='John Doe', username='johndoe')
    )
    assert payload.todo_user.name == 'John Doe'
