from graphscale.pent import PentConfig, PentContext, create_class_map
import graphscale.kvetch
from graphscale_todo.kvetch import kvetch_schema
from . import pents, mutations

CLASS_MAP = create_class_map(pents, mutations)


def pent_config():
    return PentConfig(class_map=CLASS_MAP, kvetch_schema=kvetch_schema())


def pent_context(kvetch):
    return PentContext(kvetch=kvetch, config=pent_config())


def single_db_context(conn_info):
    return pent_context(
        graphscale.kvetch.init_from_conn(
            conn_info=conn_info,
            schema=kvetch_schema(),
        )
    )


def in_mem_context():
    return pent_context(graphscale.kvetch.init_in_memory(kvetch_schema()))
