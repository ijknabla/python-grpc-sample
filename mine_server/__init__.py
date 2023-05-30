from collections.abc import Generator, Iterator
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager

from grpc import ServicerContext
from grpc import server as grpc_server

from mine.pb2 import CountRequest, CountResponse, FizzBuzzRequest, FizzBuzzResponse
from mine.rpc import MineServicer as MineServicerBase
from mine.rpc import add_MineServicer_to_server


class MineServicer(MineServicerBase):
    def FizzBuzz(self, request: FizzBuzzRequest, context: ServicerContext) -> FizzBuzzResponse:
        response = FizzBuzzResponse()
        if request.i % 3 == 0:
            response.s += "Fizz"
        if request.i % 5 == 0:
            response.s += "Buzz"
        return response

    def Count(self, request: CountRequest, context: ServicerContext) -> Iterator[CountResponse]:
        for i in range(request.n):
            yield CountResponse(i=i)


@contextmanager
def serve(host: str, port: int) -> Generator[None, None, None]:
    servicer = MineServicer()
    server = grpc_server(ThreadPoolExecutor(max_workers=3))
    add_MineServicer_to_server(servicer, server)
    server.add_insecure_port(f"{host}:{port}")
    server.start()
    try:
        yield None
    finally:
        server.stop(0)
