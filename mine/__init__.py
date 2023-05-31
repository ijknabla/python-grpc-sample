__all__ = (
    "AsyncMineServicer",
    "AsyncMineStub",
    "DefaultMineServicer",
    "DefaultMineStub",
    "FizzBuzzRequest",
    "FizzBuzzResponse",
    "MineServicer",
    "MineStub",
    "SupportsAsyncMineServicer",
    "SupportsAsyncMineStub",
    "SupportsDefaultMineServicer",
    "SupportsDefaultMineStub",
    "UnsignedInteger",
    "add_MineServicer_to_server",
)

from typing import TYPE_CHECKING

import grpc.aio

from ._proto.mine_pb2 import FizzBuzzRequest, FizzBuzzResponse, UnsignedInteger
from ._proto.mine_pb2_grpc import MineServicer, MineStub, add_MineServicer_to_server
from ._protocol import (
    SupportsAsyncMineServicer,
    SupportsAsyncMineStub,
    SupportsDefaultMineServicer,
    SupportsDefaultMineStub,
)


class DefaultMineStub(SupportsDefaultMineStub, MineStub):
    if TYPE_CHECKING:

        def __init__(self, channel: grpc.Channel) -> None:
            ...


class AsyncMineStub(SupportsAsyncMineStub, MineStub):
    if TYPE_CHECKING:

        def __init__(self, channel: grpc.aio.Channel) -> None:
            ...


class DefaultMineServicer(SupportsDefaultMineServicer, MineServicer):
    ...


class AsyncMineServicer(SupportsAsyncMineServicer, MineServicer):
    ...
