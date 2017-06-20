from graphscale.kvetch import define_schema, define_object
from .generated import generated_objects, generated_indexes, generated_edges


def kvetch_schema():
    objects = generated_objects()
    objects.append(define_object(type_name='TodoUser', type_id=1000))
    indexes = generated_indexes()
    edges = generated_edges()
    return define_schema(objects=objects, indexes=indexes, edges=edges)
