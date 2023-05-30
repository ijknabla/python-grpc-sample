from __future__ import annotations

from asyncio import (
    FIRST_COMPLETED,
    AbstractEventLoop,
    Queue,
    create_task,
    get_event_loop_policy,
    get_running_loop,
    wait,
)
from collections.abc import (
    AsyncGenerator,
    AsyncIterable,
    Awaitable,
    Callable,
    Generator,
    Iterator,
    Sequence,
)
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Protocol, TypeVar

import grpc.aio
from pytest import FixtureRequest
from pytest_asyncio import fixture

from mine import (
    AsyncMineStub,
    CountRequest,
    CountResponse,
    FizzBuzzRequest,
    FizzBuzzResponse,
    MineStub,
    SupportsAddMineServicerToServer,
    add_MineServicer_to_server,
)
from mine_server import AsyncMineServicer

from . import SupportsMineStub

T_request = TypeVar("T_request")
T_response = TypeVar("T_response")


@fixture(scope="session")
def event_loop() -> Generator[AbstractEventLoop, None, None]:
    loop = get_event_loop_policy().new_event_loop()
    try:
        yield loop
    finally:
        loop.close()


@fixture(scope="module")
def _grpc_server(
    request: FixtureRequest,
    grpc_addr: str,
    grpc_interceptors: Sequence[grpc.aio.ServerInterceptor[Any, Any]] | None,
) -> Generator[grpc.aio.Server, None, None]:
    max_workers = request.config.getoption("grpc-max-workers")
    try:
        max_workers = max(request.module.grpc_max_workers, max_workers)
    except AttributeError:
        pass

    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        yield grpc.aio.server(pool, interceptors=grpc_interceptors)


@fixture(scope="module")
def grpc_add_to_server() -> SupportsAddMineServicerToServer:
    return add_MineServicer_to_server


@fixture(scope="module")
def grpc_servicer() -> AsyncMineServicer:
    return AsyncMineServicer()


@fixture(scope="module")
async def grpc_server(
    _grpc_server: grpc.aio.Server,
    grpc_addr: str,
    grpc_add_to_server: SupportsAddMineServicerToServer,
    grpc_servicer: AsyncMineServicer,
) -> AsyncGenerator[grpc.aio.Server, None]:
    grpc_add_to_server(grpc_servicer, _grpc_server)
    _grpc_server.add_insecure_port(grpc_addr)

    await _grpc_server.start()
    try:
        yield _grpc_server
    finally:
        await _grpc_server.stop(None)
        await _grpc_server.wait_for_termination()


class AsyncCreateChannel(Protocol):
    def __call__(
        self,
        credentials: grpc.ChannelCredentials | None = None,
        options: grpc._Options | None = None,
    ) -> grpc.aio.Channel:
        ...


@fixture(scope="module")
def grpc_aio_create_channel(
    request: FixtureRequest, grpc_addr: str, grpc_server: grpc.Server
) -> AsyncCreateChannel:
    def _create_channel(
        credentials: grpc.ChannelCredentials | None = None,
        options: grpc._Options | None = None,
    ) -> grpc.aio.Channel:
        if credentials is not None:
            return grpc.aio.secure_channel(grpc_addr, credentials, options)
        return grpc.aio.insecure_channel(grpc_addr, options)

    return _create_channel


@fixture(scope="module")
async def grpc_aio_channel(
    grpc_addr: str, grpc_aio_create_channel: AsyncCreateChannel
) -> AsyncGenerator[grpc.aio.Channel, None]:
    async with grpc_aio_create_channel() as channel:
        yield channel


@fixture(scope="module")
def grpc_stub_cls(grpc_channel: grpc.Channel) -> type[SupportsMineStub]:
    class MineStubWrapper:
        stub: MineStub

        def __init__(self, channel: grpc.Channel) -> None:
            self.stub = MineStub(channel)

        def FizzBuzz(self, request: FizzBuzzRequest) -> Awaitable[FizzBuzzResponse]:
            return self.__unary_unary(self.stub.FizzBuzz, request)

        def Count(self, request: CountRequest) -> AsyncIterable[CountResponse]:
            return self.__unary_stream(self.stub.Count, request)

        @staticmethod
        def __unary_unary(
            f: Callable[[T_request], T_response], request: T_request
        ) -> Awaitable[T_response]:
            return get_running_loop().run_in_executor(None, lambda: f(request))

        @staticmethod
        async def __unary_stream(
            f: Callable[[T_request], Iterator[T_response]], request: T_request
        ) -> AsyncIterable[T_response]:
            q = Queue[T_response]()

            def put() -> None:
                for response in f(request):
                    q.put_nowait(response)

            async def put_and_join() -> None:
                await get_running_loop().run_in_executor(None, put)
                await q.join()

            put_and_join_task = create_task(put_and_join())

            while True:
                get_task = create_task(q.get())
                done, _ = await wait([put_and_join_task, get_task], return_when=FIRST_COMPLETED)
                if done == {get_task}:
                    yield get_task.result()
                    q.task_done()
                elif done == {put_and_join_task}:
                    get_task.cancel()
                    return
                else:
                    raise NotImplementedError()

    return MineStubWrapper


@fixture(scope="module")
def grpc_aio_stub_cls(grpc_channel: grpc.Channel) -> Callable[[grpc.aio.Channel], SupportsMineStub]:
    return AsyncMineStub


@fixture(scope="module")
async def grpc_aio_stub(
    grpc_aio_stub_cls: Callable[[grpc.aio.Channel], SupportsMineStub],
    grpc_aio_channel: grpc.aio.Channel,
) -> AsyncGenerator[SupportsMineStub, None]:
    yield grpc_aio_stub_cls(grpc_aio_channel)
