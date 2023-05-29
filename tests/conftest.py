from collections.abc import Callable

from grpc import Channel, Server
from pytest import fixture

from mine.rpc import MineStub, add_MineServicer_to_server
from mine_server import MineServicer


@fixture(scope="module")
def grpc_add_to_server() -> Callable[[MineServicer, Server], None]:
    return add_MineServicer_to_server


@fixture(scope="module")
def grpc_servicer() -> MineServicer:
    return MineServicer()


@fixture(scope="module")
def grpc_stub_cls(grpc_channel: Channel) -> type[MineStub]:
    return MineStub
