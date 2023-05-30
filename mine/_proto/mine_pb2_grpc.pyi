from collections.abc import AsyncIterable as _AsyncIterable
from collections.abc import Awaitable as _Awaitable
from collections.abc import Iterator as _Iterator
from typing import Protocol as _Protocol

import grpc

from . import mine_pb2 as mine__pb2

class MineStub(_Protocol):
    def __init__(self, channel: grpc.Channel) -> None: ...
    def FizzBuzz(self, request: mine__pb2.FizzBuzzRequest) -> mine__pb2.FizzBuzzResponse: ...
    def Count(self, request: mine__pb2.CountRequest) -> _Iterator[mine__pb2.CountResponse]: ...

class AsyncMineStub(_Protocol):
    def __init__(self, channel: grpc.Channel) -> None: ...
    def FizzBuzz(
        self, request: mine__pb2.FizzBuzzRequest
    ) -> _Awaitable[mine__pb2.FizzBuzzResponse]: ...
    def Count(self, request: mine__pb2.CountRequest) -> _AsyncIterable[mine__pb2.CountResponse]: ...

class MineServicer(object):
    def FizzBuzz(
        self, request: mine__pb2.FizzBuzzRequest, context: grpc.ServicerContext
    ) -> mine__pb2.FizzBuzzResponse: ...
    def Count(
        self, request: mine__pb2.CountRequest, context: grpc.ServicerContext
    ) -> _Iterator[mine__pb2.CountResponse]: ...

def add_MineServicer_to_server(servicer: MineServicer, server: grpc.Server) -> None: ...
