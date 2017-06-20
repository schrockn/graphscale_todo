from graphscale.pent import PentConfig, PentContext, create_class_map
import graphscale.kvetch
import graphscale_todo


def pent_config():
    return PentConfig(
        object_config=graphscale_todo.kvetch.config.object_config(), 
        edge_config=graphscale_todo.kvetch.config.edge_config(), 
    )

def pent_context(kvetch):
    return PentContext(kvetch=kvetch, config=pent_config())


CLASS_MAP = create_class_map(graphscale_todo.pent.pents, graphscale_todo.pent.mutations)

def single_db_context(conn_info):
    return pent_context(
        graphscale.kvetch.init_from_conn(
            conn_info=conn_info,
            schema=graphscale_todo.kvetch.kvetch_schema(),
        )
    )

def in_mem_context():
    return pent_context(graphscale.kvetch.init_in_memory(graphscale_todo.kvetch.kvetch_schema())
