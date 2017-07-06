#W0661: unused imports lint
#C0301: line too long
#C0103: disable invalid constant name
#pylint: disable=W0611,C0301,C0103

from graphql import (
    GraphQLSchema,
    GraphQLObjectType,
    GraphQLField,
    GraphQLString,
    GraphQLArgument,
    GraphQLList,
    GraphQLInt,
    GraphQLInputObjectType,
    GraphQLInputObjectField,
    GraphQLNonNull,
    GraphQLID,
    GraphQLEnumType,
    GraphQLBoolean,
)

from graphql.type import GraphQLEnumValue

from graphscale.grapple import (
    req,
    list_of,
    GraphQLDate,
    GraphQLUUID,
    GraphQLPythonEnumType,
    define_default_resolver,
    define_default_gen_resolver,
    define_pent_mutation_resolver,
)

import graphscale_todo.pent as module_pents

GraphQLQuery = GraphQLObjectType(
    name='Query',
    fields=lambda: {
        'todoUser': GraphQLField(
            type=GraphQLTodoUser, # type: ignore
            args={
                'id': GraphQLArgument(type=req(GraphQLUUID)), # type: ignore
            },
            resolver=define_default_gen_resolver('gen_todo_user'),
        ),
        'allTodoUsers': GraphQLField(
            type=req(list_of(req(GraphQLTodoUser))), # type: ignore
            args={
                'first': GraphQLArgument(type=GraphQLInt, default_value=100), # type: ignore
                'after': GraphQLArgument(type=GraphQLUUID), # type: ignore
            },
            resolver=define_default_gen_resolver('gen_all_todo_users'),
        ),
        'todoItem': GraphQLField(
            type=GraphQLTodoItem, # type: ignore
            args={
                'id': GraphQLArgument(type=req(GraphQLUUID)), # type: ignore
            },
            resolver=define_default_gen_resolver('gen_todo_item'),
        ),
        'allTodoItems': GraphQLField(
            type=req(list_of(req(GraphQLTodoItem))), # type: ignore
            args={
                'first': GraphQLArgument(type=GraphQLInt, default_value=100), # type: ignore
                'after': GraphQLArgument(type=GraphQLUUID), # type: ignore
            },
            resolver=define_default_gen_resolver('gen_all_todo_items'),
        ),
        'todoList': GraphQLField(
            type=GraphQLTodoList, # type: ignore
            args={
                'id': GraphQLArgument(type=req(GraphQLUUID)), # type: ignore
            },
            resolver=define_default_gen_resolver('gen_todo_list'),
        ),
    },
)

GraphQLTodoUser = GraphQLObjectType(
    name='TodoUser',
    fields=lambda: {
        'id': GraphQLField(
            type=req(GraphQLUUID), # type: ignore
            resolver=define_default_resolver('obj_id'),
        ),
        'name': GraphQLField(
            type=req(GraphQLString), # type: ignore
            resolver=define_default_resolver('name'),
        ),
        'username': GraphQLField(
            type=req(GraphQLString), # type: ignore
            resolver=define_default_resolver('username'),
        ),
        'todoLists': GraphQLField(
            type=req(list_of(req(GraphQLTodoList))), # type: ignore
            args={
                'first': GraphQLArgument(type=GraphQLInt, default_value=100), # type: ignore
                'after': GraphQLArgument(type=GraphQLUUID), # type: ignore
            },
            resolver=define_default_gen_resolver('gen_todo_lists'),
        ),
    },
)

GraphQLTodoList = GraphQLObjectType(
    name='TodoList',
    fields=lambda: {
        'id': GraphQLField(
            type=req(GraphQLUUID), # type: ignore
            resolver=define_default_resolver('obj_id'),
        ),
        'name': GraphQLField(
            type=req(GraphQLString), # type: ignore
            resolver=define_default_resolver('name'),
        ),
        'owner': GraphQLField(
            type=GraphQLTodoUser, # type: ignore
            resolver=define_default_gen_resolver('gen_owner'),
        ),
        'todoItems': GraphQLField(
            type=req(list_of(req(GraphQLTodoItem))), # type: ignore
            args={
                'first': GraphQLArgument(type=GraphQLInt, default_value=100), # type: ignore
                'after': GraphQLArgument(type=GraphQLUUID), # type: ignore
            },
            resolver=define_default_gen_resolver('gen_todo_items'),
        ),
    },
)

GraphQLTodoItem = GraphQLObjectType(
    name='TodoItem',
    fields=lambda: {
        'id': GraphQLField(
            type=req(GraphQLUUID), # type: ignore
            resolver=define_default_resolver('obj_id'),
        ),
        'text': GraphQLField(
            type=req(GraphQLString), # type: ignore
            resolver=define_default_resolver('text'),
        ),
        'list': GraphQLField(
            type=GraphQLTodoList, # type: ignore
            resolver=define_default_gen_resolver('gen_list'),
        ),
        'todoItemStatus': GraphQLField(
            type=req(GraphQLTodoItemStatus), # type: ignore
            resolver=define_default_resolver('todo_item_status'),
        ),
    },
)

GraphQLMutation = GraphQLObjectType(
    name='Mutation',
    fields=lambda: {
        'createTodoUser': GraphQLField(
            type=GraphQLCreateTodoUserPayload, # type: ignore
            args={
                'data': GraphQLArgument(type=req(GraphQLCreateTodoUserData)), # type: ignore
            },
            resolver=define_pent_mutation_resolver('gen_create_todo_user', 'CreateTodoUserData'),
        ),
        'updateTodoUser': GraphQLField(
            type=GraphQLUpdateTodoUserPayload, # type: ignore
            args={
                'id': GraphQLArgument(type=req(GraphQLUUID)), # type: ignore
                'data': GraphQLArgument(type=req(GraphQLUpdateTodoUserData)), # type: ignore
            },
            resolver=define_pent_mutation_resolver('gen_update_todo_user', 'UpdateTodoUserData'),
        ),
        'deleteTodoUser': GraphQLField(
            type=GraphQLDeleteTodoUserPayload, # type: ignore
            args={
                'id': GraphQLArgument(type=req(GraphQLUUID)), # type: ignore
            },
            resolver=define_default_gen_resolver('gen_delete_todo_user'),
        ),
        'createTodoList': GraphQLField(
            type=GraphQLCreateTodoListPayload, # type: ignore
            args={
                'data': GraphQLArgument(type=req(GraphQLCreateTodoListData)), # type: ignore
            },
            resolver=define_pent_mutation_resolver('gen_create_todo_list', 'CreateTodoListData'),
        ),
        'createTodoItem': GraphQLField(
            type=GraphQLCreateTodoItemPayload, # type: ignore
            args={
                'data': GraphQLArgument(type=req(GraphQLCreateTodoItemData)), # type: ignore
            },
            resolver=define_pent_mutation_resolver('gen_create_todo_item', 'CreateTodoItemData'),
        ),
        'deleteTodoItem': GraphQLField(
            type=GraphQLDeleteTodoItemPayload, # type: ignore
            args={
                'id': GraphQLArgument(type=req(GraphQLUUID)), # type: ignore
            },
            resolver=define_default_gen_resolver('gen_delete_todo_item'),
        ),
    },
)

GraphQLCreateTodoUserPayload = GraphQLObjectType(
    name='CreateTodoUserPayload',
    fields=lambda: {
        'todoUser': GraphQLField(
            type=GraphQLTodoUser, # type: ignore
            resolver=define_default_resolver('todo_user'),
        ),
    },
)

GraphQLUpdateTodoUserPayload = GraphQLObjectType(
    name='UpdateTodoUserPayload',
    fields=lambda: {
        'todoUser': GraphQLField(
            type=GraphQLTodoUser, # type: ignore
            resolver=define_default_resolver('todo_user'),
        ),
    },
)

GraphQLDeleteTodoUserPayload = GraphQLObjectType(
    name='DeleteTodoUserPayload',
    fields=lambda: {
        'deletedId': GraphQLField(
            type=GraphQLUUID, # type: ignore
            resolver=define_default_resolver('deleted_id'),
        ),
    },
)

GraphQLCreateTodoListPayload = GraphQLObjectType(
    name='CreateTodoListPayload',
    fields=lambda: {
        'todoList': GraphQLField(
            type=GraphQLTodoList, # type: ignore
            resolver=define_default_resolver('todo_list'),
        ),
    },
)

GraphQLCreateTodoItemPayload = GraphQLObjectType(
    name='CreateTodoItemPayload',
    fields=lambda: {
        'todoItem': GraphQLField(
            type=GraphQLTodoItem, # type: ignore
            resolver=define_default_resolver('todo_item'),
        ),
    },
)

GraphQLDeleteTodoItemPayload = GraphQLObjectType(
    name='DeleteTodoItemPayload',
    fields=lambda: {
        'deletedId': GraphQLField(
            type=GraphQLUUID, # type: ignore
            resolver=define_default_resolver('deleted_id'),
        ),
    },
)

GraphQLCreateTodoUserData = GraphQLInputObjectType(
    name='CreateTodoUserData',
    fields=lambda: {
        'name': GraphQLInputObjectField(type=req(GraphQLString)),
        'username': GraphQLInputObjectField(type=req(GraphQLString)),
    },
)

GraphQLUpdateTodoUserData = GraphQLInputObjectType(
    name='UpdateTodoUserData',
    fields=lambda: {
        'name': GraphQLInputObjectField(type=GraphQLString),
    },
)

GraphQLCreateTodoListData = GraphQLInputObjectType(
    name='CreateTodoListData',
    fields=lambda: {
        'name': GraphQLInputObjectField(type=req(GraphQLString)),
        'ownerId': GraphQLInputObjectField(type=req(GraphQLUUID)),
    },
)

GraphQLCreateTodoItemData = GraphQLInputObjectType(
    name='CreateTodoItemData',
    fields=lambda: {
        'text': GraphQLInputObjectField(type=req(GraphQLString)),
        'listId': GraphQLInputObjectField(type=req(GraphQLUUID)),
        'todoItemStatus': GraphQLInputObjectField(type=req(GraphQLTodoItemStatus)),
    },
)

GraphQLTodoItemStatus = GraphQLPythonEnumType(module_pents.TodoItemStatus)