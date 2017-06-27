from graphscale.kvetch import define_object, define_edge, define_index

def generated_objects():
    return [
        define_object(type_name='TodoUser', type_id=100000),
        define_object(type_name='TodoList', type_id=100002),
        define_object(type_name='TodoItem', type_id=100001),
    ]

def generated_edges():
    return [
        define_edge(edge_name='user_to_list_edge', edge_id=2039430, from_id_attr='owner_id'),
        define_edge(edge_name='list_to_item_edge', edge_id=83948934, from_id_attr='list_id'),
    ]

def generated_indexes():
    return []
