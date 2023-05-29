from collections.abc import Callable

from grpc import Server
from pytest import fixture

from mine.rpc import add_MineServicer_to_server
from mine_server import MineServicer


@fixture(scope="module")
def grpc_add_to_server() -> Callable[[MineServicer, Server], None]:
    return add_MineServicer_to_server


@fixture(scope="module")
def grpc_servicer() -> MineServicer:
    return MineServicer()
