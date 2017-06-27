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
    GrappleType,
    id_field,
    req,
    list_of,
    define_top_level_getter,
    GraphQLDate,
    GraphQLUUID,
    create_browse_field,
    define_create,
    define_default_resolver,
    define_pent_mutation_resolver,
)

GraphQLTodoUser = GraphQLObjectType(
    name='TodoUser',
    fields=lambda: {
        'id': GraphQLField(
            type=req(GraphQLUUID),
            resolver=define_default_resolver('obj_id'),
        ),
        'name': GraphQLField(
            type=req(GraphQLString),
            resolver=define_default_resolver('name'),
        ),
        'username': GraphQLField(
            type=req(GraphQLString),
            resolver=define_default_resolver('username'),
        ),
    },
)

GraphQLTodoItem = GraphQLObjectType(
    name='TodoItem',
    fields=lambda: {
        'id': GraphQLField(
            type=req(GraphQLUUID),
            resolver=define_default_resolver('obj_id'),
        ),
        'text': GraphQLField(
            type=req(GraphQLString),
            resolver=define_default_resolver('text'),
        ),
    },
)

GraphQLQuery = GraphQLObjectType(
    name='Query',
    fields=lambda: {
        'todoUser': GraphQLField(
            type=GraphQLTodoUser,
            args={
                'id': GraphQLArgument(type=req(GraphQLUUID)),
            },
            resolver=define_default_resolver('gen_todo_user'),
        ),
        'allTodoUsers': GraphQLField(
            type=req(list_of(req(GraphQLTodoUser))),
            args={
                'first': GraphQLArgument(type=GraphQLInt, default_value=100),
                'after': GraphQLArgument(type=GraphQLUUID),
            },
            resolver=define_default_resolver('gen_all_todo_users'),
        ),
        'todoItem': GraphQLField(
            type=GraphQLTodoItem,
            args={
                'id': GraphQLArgument(type=req(GraphQLUUID)),
            },
            resolver=define_default_resolver('gen_todo_item'),
        ),
        'allTodoItems': GraphQLField(
            type=req(list_of(req(GraphQLTodoItem))),
            args={
                'first': GraphQLArgument(type=GraphQLInt, default_value=100),
                'after': GraphQLArgument(type=GraphQLUUID),
            },
            resolver=define_default_resolver('gen_all_todo_items'),
        ),
    },
)

GraphQLMutation = GraphQLObjectType(
    name='Mutation',
    fields=lambda: {
        'createTodoUser': GraphQLField(
            type=GraphQLTodoUser,
            args={
                'data': GraphQLArgument(type=req(GraphQLCreateTodoUserData)),
            },
            resolver=define_pent_mutation_resolver('gen_create_todo_user', 'CreateTodoUserData'),
        ),
        'updateTodoUser': GraphQLField(
            type=GraphQLTodoUser,
            args={
                'id': GraphQLArgument(type=req(GraphQLUUID)),
                'data': GraphQLArgument(type=req(GraphQLUpdateTodoUserData)),
            },
            resolver=define_pent_mutation_resolver('gen_update_todo_user', 'UpdateTodoUserData'),
        ),
        'deleteTodoUser': GraphQLField(
            type=GraphQLTodoUser,
            args={
                'id': GraphQLArgument(type=req(GraphQLUUID)),
            },
            resolver=define_default_resolver('gen_delete_todo_user'),
        ),
        'createTodoItem': GraphQLField(
            type=GraphQLTodoItem,
            args={
                'data': GraphQLArgument(type=req(GraphQLCreateTodoItemData)),
            },
            resolver=define_pent_mutation_resolver('gen_create_todo_item', 'CreateTodoItemData'),
        ),
        'deleteTodoItem': GraphQLField(
            type=GraphQLTodoItem,
            args={
                'id': GraphQLArgument(type=req(GraphQLUUID)),
            },
            resolver=define_default_resolver('gen_delete_todo_item'),
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

GraphQLCreateTodoItemData = GraphQLInputObjectType(
    name='CreateTodoItemData',
    fields=lambda: {
        'text': GraphQLInputObjectField(type=req(GraphQLString)),
    },
)
