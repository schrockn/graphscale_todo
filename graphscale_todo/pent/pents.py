from . import generated


class Root(generated.QueryGenerated, generated.MutationGenerated):
    pass


class TodoUser(generated.TodoUserGenerated):
    pass


class TodoItem(generated.TodoItemGenerated):
    pass


class TodoList(generated.TodoListGenerated):
    pass
