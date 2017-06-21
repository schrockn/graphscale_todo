from context import graphscale_todo
from graphscale_todo.pent import Query, Mutation, in_mem_context, CreateTodoUserInput, TodoUser
import pytest
pytestmark = pytest.mark.asyncio


async def test_test():
    context = in_mem_context()
    mutation = Mutation(context)
    input_object = CreateTodoUserInput({'name': 'Test Name'})
    out_todo = await mutation.create_todo_user(input_object)
    assert isinstance(out_todo, TodoUser)
    assert out_todo.name == 'Test Name'

    query = Query(context)
    todo = await query.todo_user(out_todo.obj_id)
    assert isinstance(todo, TodoUser)
    assert todo.name == 'Test Name'
