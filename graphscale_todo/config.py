from graphscale.pent import PentConfig, PentContext, create_class_map
from graphscale.kvetch import init_from_conn, init_in_memory
from .kvetch import kvetch_schema
from .pent import pents

CLASS_MAP = create_class_map(pents, None)


def pent_config():
    return PentConfig(class_map=CLASS_MAP, kvetch_schema=kvetch_schema())


def pent_context(kvetch):
    return PentContext(kvetch=kvetch, config=pent_config())


def single_db_context(conn_info):
    return pent_context(init_from_conn(conn_info=conn_info, schema=kvetch_schema()))


def in_mem_context():
    return pent_context(init_in_memory(kvetch_schema()))
