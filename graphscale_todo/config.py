import graphscale_todo.pent
from graphscale.kvetch import Kvetch, init_from_conn, init_in_memory
from graphscale.pent import PentConfig, PentContext, create_class_map
from graphscale.sql import ConnectionInfo

from .kvetch import kvetch_schema

CLASS_MAP = create_class_map(graphscale_todo.pent)


def pent_config() -> PentConfig:
    return PentConfig(class_map=CLASS_MAP, kvetch_schema=kvetch_schema())


def pent_context(kvetch: Kvetch) -> PentContext:
    return PentContext(kvetch=kvetch, config=pent_config())


def single_db_context(conn_info: ConnectionInfo) -> PentContext:
    return pent_context(init_from_conn(conn_info=conn_info, schema=kvetch_schema()))


def in_mem_context() -> PentContext:
    return pent_context(init_in_memory(kvetch_schema()))
