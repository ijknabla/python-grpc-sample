from collections.abc import AsyncIterator, Generator, Iterator
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager

import grpc

from mine import AsyncMineServicer as _AsyncMineServicerBase
from mine import FizzBuzzRequest, FizzBuzzResponse
from mine import MineServicer as _MineServicerBase
from mine import UnsignedInteger, add_MineServicer_to_server


class MineServicer(_MineServicerBase):
    def FizzBuzz(self, request: FizzBuzzRequest, context: grpc.ServicerContext) -> FizzBuzzResponse:
        response = FizzBuzzResponse()
        if request.i % 3 == 0:
            response.s += "Fizz"
        if request.i % 5 == 0:
            response.s += "Buzz"
        return response

    def Count(
        self, request: UnsignedInteger, context: grpc.ServicerContext
    ) -> Iterator[UnsignedInteger]:
        for u in range(request.u):
            yield UnsignedInteger(u=u)


class AsyncMineServicer(_AsyncMineServicerBase):
    async def FizzBuzz(
        self,
        request: FizzBuzzRequest,
        context: grpc.aio.ServicerContext[FizzBuzzRequest, FizzBuzzResponse],
    ) -> FizzBuzzResponse:
        response = FizzBuzzResponse()
        if request.i % 3 == 0:
            response.s += "Fizz"
        if request.i % 5 == 0:
            response.s += "Buzz"
        return response

    async def Count(
        self,
        request: UnsignedInteger,
        context: grpc.aio.ServicerContext[UnsignedInteger, UnsignedInteger],
    ) -> AsyncIterator[UnsignedInteger]:
        for u in range(request.u):
            yield UnsignedInteger(u=u)


@contextmanager
def serve(host: str, port: int) -> Generator[None, None, None]:
    servicer = MineServicer()
    server = grpc.server(ThreadPoolExecutor(max_workers=3))
    add_MineServicer_to_server(servicer, server)
    server.add_insecure_port(f"{host}:{port}")
    server.start()
    try:
        yield None
    finally:
        server.stop(0)
