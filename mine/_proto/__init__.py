__all__ = (
    "mine_pb2",
    "mine_pb2_grpc",
)

from .. import push_module_to_path

with push_module_to_path(__name__):
    from . import mine_pb2, mine_pb2_grpc
