from graphscale.kvetch import define_schema, define_object, define_edge
from .generated import generated_objects, generated_indexes, generated_edges


def kvetch_schema():
    objects = generated_objects()
    indexes = generated_indexes()
    edges = generated_edges()
    edges.append(
        define_edge(
            edge_name='user_to_list_edge',
            edge_id=192381923,
            from_id_attr='owner_id',
        )
    )
    return define_schema(objects=objects, indexes=indexes, edges=edges)
