from graphscale.pent import PentConfig, create_fresh_pent_context, create_class_map
from graphscale.kvetch import init_from_conn, init_in_memory
from .kvetch import kvetch_schema
from .pent import pents, mutations

CLASS_MAP = create_class_map(pents, mutations)


def pent_config():
    return PentConfig(class_map=CLASS_MAP, kvetch_schema=kvetch_schema())


def pent_context(kvetch):
    return create_fresh_pent_context(kvetch=kvetch, config=pent_config())


def single_db_context(conn_info):
    return pent_context(init_from_conn(conn_info=conn_info, schema=kvetch_schema()))


def in_mem_context():
    return pent_context(init_in_memory(kvetch_schema()))
