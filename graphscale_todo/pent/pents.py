from . import generated

from graphscale.pent import delete_pent

from .mutations import DeleteTodoUserPayload


async def gen_delete_pent_dynamic(context, pent_cls_name, payload_cls_name, obj_id):
    # check.param(context, PentContext, 'context')
    # check.str_param(out_cls_name, 'out_cls_name')
    # check.uuid_param(obj_id, 'obj_id')

    pent_cls = context.cls_from_name(pent_cls_name)
    payload_cls = context.cls_from_name(payload_cls_name)
    deleted_id = await delete_pent(context, pent_cls, obj_id)
    return payload_cls(deleted_id)


class Root(generated.QueryGenerated, generated.MutationGenerated):
    def __init__(self, context):
        self.__context = context

    @property
    def context(self):
        return self.__context

    async def gen_delete_todo_user(self, obj_id):
        return await gen_delete_pent_dynamic(
            self.context, 'TodoUser', 'DeleteTodoUserPayload', obj_id
        )
        # deleted_id = await delete_pent(self.context, TodoUser, obj_id)
        # return DeleteTodoUserPayload(deleted_id)

    async def gen_delete_todo_item(self, obj_id):
        return await gen_delete_pent_dynamic(
            self.context, 'TodoItem', 'DeleteTodoItemPayload', obj_id
        )


class TodoUser(generated.TodoUserGenerated):
    pass


class TodoItem(generated.TodoItemGenerated):
    pass


class TodoList(generated.TodoListGenerated):
    pass
