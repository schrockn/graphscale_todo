from graphscale.kvetch import define_object

def generated_objects():
    return [
        define_object(type_name='TodoUser', type_id=100000),
        define_object(type_name='TodoItem', type_id=100001),
    ]

def generated_edges():
    return []

def generated_indexes():
    return []
