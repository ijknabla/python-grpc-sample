from collections.abc import AsyncIterator, Generator, Iterator
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager

import grpc

from mine import AsyncMineServicer as _AsyncMineServicerBase
from mine import CountRequest, CountResponse, FizzBuzzRequest, FizzBuzzResponse
from mine import MineServicer as _MineServicerBase
from mine import add_MineServicer_to_server


class MineServicer(_MineServicerBase):
    def FizzBuzz(self, request: FizzBuzzRequest, context: grpc.ServicerContext) -> FizzBuzzResponse:
        response = FizzBuzzResponse()
        if request.i % 3 == 0:
            response.s += "Fizz"
        if request.i % 5 == 0:
            response.s += "Buzz"
        return response

    def Count(
        self, request: CountRequest, context: grpc.ServicerContext
    ) -> Iterator[CountResponse]:
        for i in range(request.n):
            yield CountResponse(i=i)


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
        self, request: CountRequest, context: grpc.aio.ServicerContext[CountRequest, CountResponse]
    ) -> AsyncIterator[CountResponse]:
        for i in range(request.n):
            yield CountResponse(i=i)


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
