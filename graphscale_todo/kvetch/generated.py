#W0611: unused imports lint
#C0301: line too long
#pylint: disable=W0611, C0301

from typing import List
from graphscale.kvetch import ObjectDefinition, StoredIdEdgeDefinition, IndexDefinition

def generated_objects() -> List[ObjectDefinition]:
    return [
        ObjectDefinition(type_name='TodoUser', type_id=100000),
        ObjectDefinition(type_name='TodoList', type_id=100002),
        ObjectDefinition(type_name='TodoItem', type_id=100001),
    ]

def generated_edges() -> List[StoredIdEdgeDefinition]:
    return [
        StoredIdEdgeDefinition(edge_name='user_to_list_edge', edge_id=10000, stored_id_attr='owner_id', stored_on_type='TodoList'),
        StoredIdEdgeDefinition(edge_name='list_to_item_edge', edge_id=10001, stored_id_attr='list_id', stored_on_type='TodoItem'),
    ]

def generated_indexes() -> List[IndexDefinition]:
    return []
