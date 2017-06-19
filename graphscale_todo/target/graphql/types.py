#W0661: unused imports lint

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

from graphscale.grapple import (
    req,
    list_of,
    define_default_resolver,
)

GraphQLTodoUser = GraphQLObjectType(name='User', fields=lambda: {
    'id': GraphQLField(
        type=req(GraphQLID),
        resolver=define_default_resolver('obj_id'),
    ),
    'name': GraphQLField(
        type=req(GraphQLString),
        resolver=define_default_resolver('name'),
    ),
})

GraphQLQuery = GraphQLObjectType(name='Query', fields=lambda: {

})

GraphQLMutation = GraphQLObjectType(name='Mutation', fields=lambda: {

})
