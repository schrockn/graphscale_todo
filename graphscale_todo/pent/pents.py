from collections import namedtuple

from graphscale import check
from graphscale.grapple.graphql_impl import gen_create_pent_dynamic
from graphscale.pent import create_pent, PentMutationPayload

from . import generated
from .mutations import CreateTodoUserData, CreateTodoUserPayload, CreateTodoListPayload, CreateTodoItemPayload


async def gen_create_pent_dynamic_new(
    context, pent_cls_name, data_cls_name, payload_cls_name, data
):
    pent = await gen_create_pent_dynamic(context, pent_cls_name, data_cls_name, data)
    payload_cls = context.cls_from_name(payload_cls_name)
    return payload_cls(pent)


class Root(generated.QueryGenerated, generated.MutationGenerated):
    def __init__(self, context):
        self.__context = context

    @property
    def context(self):
        return self.__context

    async def gen_create_todo_user(self, data):
        return await gen_create_pent_dynamic_new(
            self.context, 'TodoUser', 'CreateTodoUserData', 'CreateTodoUserPayload', data
        )

    async def gen_create_todo_list(self, data):
        return await gen_create_pent_dynamic_new(
            self.context, 'TodoList', 'CreateTodoListData', 'CreateTodoListPayload', data
        )

    async def gen_create_todo_item(self, data):
        return await gen_create_pent_dynamic_new(
            self.context, 'TodoItem', 'CreateTodoItemData', 'CreateTodoItemPayload', data
        )


class TodoUser(generated.TodoUserGenerated):
    pass


class TodoItem(generated.TodoItemGenerated):
    pass


class TodoList(generated.TodoListGenerated):
    pass
