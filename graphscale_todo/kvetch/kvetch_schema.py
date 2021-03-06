from graphscale.kvetch import Schema, define_string_index
from .generated import generated_objects, generated_indexes, generated_edges


def kvetch_schema() -> Schema:
    objects = generated_objects()
    indexes = generated_indexes()
    indexes.append(
        define_string_index(
            index_name='username_to_todo_user', indexed_type='TodoUser', indexed_attr='username'
        )
    )
    edges = generated_edges()
    return Schema(objects=objects, indexes=indexes, edges=edges)
