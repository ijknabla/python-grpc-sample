from collections.abc import AsyncIterable as _AsyncIterable
from collections.abc import Awaitable as _Awaitable
from collections.abc import Iterator as _Iterator
from typing import Protocol as _Protocol

import grpc.aio

from .. import SupportsAddMineServicerToServer as _SupportsAddMineServicerToServer
from . import mine_pb2 as mine__pb2

class MineServicer(object):
    def FizzBuzz(
        self, request: mine__pb2.FizzBuzzRequest, context: grpc.ServicerContext
    ) -> mine__pb2.FizzBuzzResponse: ...
    def Count(
        self, request: mine__pb2.CountRequest, context: grpc.ServicerContext
    ) -> _Iterator[mine__pb2.CountResponse]: ...

add_MineServicer_to_server: _SupportsAddMineServicerToServer
