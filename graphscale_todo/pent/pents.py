from graphscale.grapple.graphql_impl import gen_create_pent_dynamic

from . import generated


class Root(generated.QueryGenerated, generated.MutationGenerated):
    def __init__(self, context):
        self.context = context

    async def create_todo_user(self, data):
        return await self.gen_create_todo_user(data)

    async def gen_create_todo_user(self, data):
        return await gen_create_pent_dynamic(self.context, 'TodoUser', 'CreateTodoUserInput', data)

    async def create_todo_item(self, data):
        return await self.gen_create_todo_item(data)

    async def gen_create_todo_item(self, data):
        return await gen_create_pent_dynamic(self.context, 'TodoItem', 'CreateTodoItemInput', data)


class TodoUser(generated.TodoUserGenerated):
    pass


class TodoItem(generated.TodoItemGenerated):
    pass
