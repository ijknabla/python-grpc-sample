__all__ = (
    "AsyncMineStub",
    "CountRequest",
    "CountResponse",
    "FizzBuzzRequest",
    "FizzBuzzResponse",
    "MineServicer",
    "MineStub",
    "add_MineServicer_to_server",
)
from collections.abc import AsyncIterable, Awaitable, Iterator
from typing import TYPE_CHECKING, Protocol

import grpc.aio

from ._proto.mine_pb2 import CountRequest, CountResponse, FizzBuzzRequest, FizzBuzzResponse
from ._proto.mine_pb2_grpc import add_MineServicer_to_server

if TYPE_CHECKING:

    class MineStub(object):
        def __init__(self, channel: grpc.Channel) -> None:
            ...

        def FizzBuzz(self, request: FizzBuzzRequest) -> FizzBuzzResponse:
            ...

        def Count(self, request: CountRequest) -> Iterator[CountResponse]:
            ...

    class AsyncMineStub(object):
        def __init__(self, channel: grpc.aio.Channel) -> None:
            ...

        def FizzBuzz(self, request: FizzBuzzRequest) -> Awaitable[FizzBuzzResponse]:
            ...

        def Count(self, request: CountRequest) -> AsyncIterable[CountResponse]:
            ...

    class MineServicer(Protocol):
        def FizzBuzz(
            self, request: FizzBuzzRequest, context: grpc.ServicerContext
        ) -> FizzBuzzResponse:
            ...

        def Count(
            self, request: CountRequest, context: grpc.ServicerContext
        ) -> Iterator[CountResponse]:
            ...

else:
    from ._proto.mine_pb2_grpc import MineServicer as MineServicer
    from ._proto.mine_pb2_grpc import MineStub as AsyncMineStub
    from ._proto.mine_pb2_grpc import MineStub as MineStub


class SupportsAddMineServicerToServer(Protocol):
    @staticmethod
    def __call__(servicer: MineServicer, server: grpc.Server) -> None:
        ...
