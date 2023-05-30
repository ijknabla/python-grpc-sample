__all__ = (
    "AsyncMineServicer",
    "AsyncMineStub",
    "FizzBuzzRequest",
    "FizzBuzzResponse",
    "MineServicer",
    "MineStub",
    "UnsignedInteger",
    "add_MineServicer_to_server",
)

from collections.abc import AsyncIterable, Awaitable, Iterable, Iterator
from typing import TYPE_CHECKING, Protocol, overload

import grpc.aio

from ._proto.mine_pb2 import FizzBuzzRequest, FizzBuzzResponse, UnsignedInteger
from ._proto.mine_pb2_grpc import add_MineServicer_to_server

if TYPE_CHECKING:

    class MineStub(object):
        def __init__(self, channel: grpc.Channel) -> None:
            ...

        def FizzBuzz(self, request: FizzBuzzRequest) -> FizzBuzzResponse:
            ...

        def Count(self, request: UnsignedInteger) -> Iterator[UnsignedInteger]:
            ...

    class AsyncMineStub(object):
        def __init__(self, channel: grpc.aio.Channel) -> None:
            ...

        def FizzBuzz(self, request: FizzBuzzRequest) -> Awaitable[FizzBuzzResponse]:
            ...

        def Count(self, request: UnsignedInteger) -> AsyncIterable[UnsignedInteger]:
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

else:
    from ._proto.mine_pb2_grpc import MineServicer as _MineServicerBase
    from ._proto.mine_pb2_grpc import MineStub as _MineStubBase

    class MineServicer(_MineServicerBase):
        ...

    class AsyncMineServicer(_MineServicerBase):
        ...

    class MineStub(_MineStubBase):
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
