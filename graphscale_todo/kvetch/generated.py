#W0661: unused imports lint
#C0301: line too long
#pylint: disable=W0661, C0301

from graphscale.kvetch import define_object, define_stored_id_edge

def generated_objects():
    return [
        define_object(type_name='TodoUser', type_id=100000),
        define_object(type_name='TodoList', type_id=100002),
        define_object(type_name='TodoItem', type_id=100001),
    ]

def generated_edges():
    return [
        define_stored_id_edge(edge_name='user_to_list_edge', edge_id=10000, stored_id_attr='owner_id', stored_on_type='TodoList'),
        define_stored_id_edge(edge_name='list_to_item_edge', edge_id=10001, stored_id_attr='list_id', stored_on_type='TodoItem'),
    ]

def generated_indexes():
    return []
