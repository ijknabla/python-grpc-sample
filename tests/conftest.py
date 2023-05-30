from __future__ import annotations

from asyncio import AbstractEventLoop, get_event_loop_policy, get_running_loop
from collections.abc import AsyncGenerator, AsyncIterable, Awaitable, Callable, Generator
from dataclasses import dataclass
from typing import Protocol, TypeVar

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
from mine_server import MineServicer

T = TypeVar("T")


@dataclass(frozen=True)
class MineStubWrapper:
    stub: MineStub

    @staticmethod
    def run(f: Callable[[], T]) -> Awaitable[T]:
        return get_running_loop().run_in_executor(None, f)

    def FizzBuzz(self, request: FizzBuzzRequest) -> Awaitable[FizzBuzzResponse]:
        return self.run(lambda: self.stub.FizzBuzz(request))

    async def Count(self, request: CountRequest) -> AsyncIterable[CountResponse]:
        responses = await self.run(lambda: list(self.stub.Count(request)))
        for response in responses:
            yield response


@fixture(scope="session")
def event_loop() -> Generator[AbstractEventLoop, None, None]:
    loop = get_event_loop_policy().new_event_loop()
    try:
        yield loop
    finally:
        loop.close()


@fixture(scope="module")
def grpc_add_to_server() -> SupportsAddMineServicerToServer:
    return add_MineServicer_to_server


@fixture(scope="module")
def grpc_servicer() -> MineServicer:
    return MineServicer()


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
def grpc_stub_cls(grpc_channel: grpc.Channel) -> type[MineStub]:
    return MineStub


@fixture(scope="module")
async def grpc_aio_stub(
    grpc_stub_cls: type[AsyncMineStub], grpc_aio_channel: grpc.aio.Channel
) -> AsyncGenerator[AsyncMineStub, None]:
    yield grpc_stub_cls(grpc_aio_channel)
