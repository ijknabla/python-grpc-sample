__all__ = (
    "AsyncMineServicer",
    "AsyncMineStub",
    "DefaultMineServicer",
    "DefaultMineStub",
    "FizzBuzzRequest",
    "FizzBuzzResponse",
    "MineServicer",
    "MineStub",
    "SupportsAsyncMineStub",
    "SupportsDefaultMineServicer",
    "SupportsDefaultMineStub",
    "UnsignedInteger",
    "add_MineServicer_to_server",
)

from collections.abc import AsyncIterable
from typing import TYPE_CHECKING, Protocol, overload

import grpc.aio

from ._proto.mine_pb2 import FizzBuzzRequest, FizzBuzzResponse, UnsignedInteger
from ._proto.mine_pb2_grpc import MineServicer, MineStub, add_MineServicer_to_server
from ._protocol import SupportsAsyncMineStub, SupportsDefaultMineServicer, SupportsDefaultMineStub


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


if TYPE_CHECKING:

    class AsyncMineServicer(Protocol):
        async def FizzBuzz(
            self,
            request: FizzBuzzRequest,
            context: grpc.aio.ServicerContext[FizzBuzzRequest, FizzBuzzResponse],
        ) -> FizzBuzzResponse:
            ...

        def Count(
            self,
            request: UnsignedInteger,
            context: grpc.aio.ServicerContext[UnsignedInteger, UnsignedInteger],
        ) -> AsyncIterable[UnsignedInteger]:
            ...

        async def Sum(
            self,
            request: AsyncIterable[UnsignedInteger],
            context: grpc.aio.ServicerContext[UnsignedInteger, UnsignedInteger],
        ) -> UnsignedInteger:
            ...

else:

    class AsyncMineServicer(MineServicer):
        ...


class SupportsAddMineServicerToServer(Protocol):
    @overload
    @staticmethod
    def __call__(servicer: MineServicer, server: grpc.Server) -> None:
        ...

    @overload
    @staticmethod
    def __call__(servicer: AsyncMineServicer, server: grpc.aio.Server) -> None:
        ...
