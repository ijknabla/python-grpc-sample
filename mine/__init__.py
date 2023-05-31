__all__ = (
    "AsyncMineServicer",
    "AsyncMineStub",
    "DefaultMineStub",
    "FizzBuzzRequest",
    "FizzBuzzResponse",
    "MineServicer",
    "MineStub",
    "SupportsDefaultMineStub",
    "UnsignedInteger",
    "add_MineServicer_to_server",
)

from collections.abc import AsyncIterable, Awaitable, Iterable
from typing import TYPE_CHECKING, Protocol, overload

import grpc.aio

from ._proto.mine_pb2 import FizzBuzzRequest, FizzBuzzResponse, UnsignedInteger
from ._proto.mine_pb2_grpc import MineStub, add_MineServicer_to_server
from ._protocol import SupportsDefaultMineStub


class DefaultMineStub(SupportsDefaultMineStub, MineStub):
    if TYPE_CHECKING:

        def __init__(self, channel: grpc.Channel) -> None:
            ...


if TYPE_CHECKING:

    class AsyncMineStub(object):
        def __init__(self, channel: grpc.aio.Channel) -> None:
            ...

        def FizzBuzz(self, request: FizzBuzzRequest) -> Awaitable[FizzBuzzResponse]:
            ...

        def Count(self, request: UnsignedInteger) -> AsyncIterable[UnsignedInteger]:
            ...

        def Sum(self, request: AsyncIterable[UnsignedInteger]) -> Awaitable[UnsignedInteger]:
            ...

    class MineServicer(Protocol):
        def FizzBuzz(
            self, request: FizzBuzzRequest, context: grpc.ServicerContext
        ) -> FizzBuzzResponse:
            ...

        def Count(
            self, request: UnsignedInteger, context: grpc.ServicerContext
        ) -> Iterable[UnsignedInteger]:
            ...

        def Sum(
            self, request: Iterable[UnsignedInteger], context: grpc.ServicerContext
        ) -> UnsignedInteger:
            ...

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
    from ._proto.mine_pb2_grpc import MineServicer as _MineServicerBase
    from ._proto.mine_pb2_grpc import MineStub as _MineStubBase

    class MineServicer(_MineServicerBase):
        ...

    class AsyncMineServicer(_MineServicerBase):
        ...

    class AsyncMineStub(_MineStubBase):
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
