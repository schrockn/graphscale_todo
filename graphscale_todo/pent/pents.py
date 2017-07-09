from uuid import UUID
from graphscale.pent import Pent
from . import generated


class Root(generated.RootGenerated):
    pass


class TodoUser(generated.TodoUserGenerated):
    pass


class TodoList(generated.TodoListGenerated):
    pass


class TodoItem(generated.TodoItemGenerated):
    pass
