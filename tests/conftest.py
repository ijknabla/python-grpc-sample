from asyncio import AbstractEventLoop, get_event_loop_policy
from collections.abc import AsyncGenerator, Callable, Generator
from contextlib import AbstractAsyncContextManager

from grpc import aio  # type: ignore
from grpc import Channel, Server
from pytest import FixtureRequest
from pytest_asyncio import fixture

from mine.pb2 import AsyncMineStub, MineStub, add_MineServicer_to_server
from mine_server import MineServicer


@fixture(scope="session")
def event_loop() -> Generator[AbstractEventLoop, None, None]:
    loop = get_event_loop_policy().new_event_loop()
    try:
        yield loop
    finally:
        loop.close()


@fixture(scope="module")
def grpc_add_to_server() -> Callable[[MineServicer, Server], None]:
    return add_MineServicer_to_server


@fixture(scope="module")
def grpc_servicer() -> MineServicer:
    return MineServicer()


AsyncCreateChannel = Callable[[], AbstractAsyncContextManager[Channel]]


@fixture(scope="module")
def grpc_aio_create_channel(
    request: FixtureRequest, grpc_addr: str, grpc_server: Server
) -> AsyncCreateChannel:
    def _create_channel(
        # credentials=None,
        # options=None,
    ) -> AbstractAsyncContextManager[Channel]:
        return aio.insecure_channel(grpc_addr)  # type: ignore

    return _create_channel


@fixture(scope="module")
async def grpc_aio_channel(
    grpc_addr: str, grpc_aio_create_channel: AsyncCreateChannel
) -> AsyncGenerator[Channel, None]:
    async with grpc_aio_create_channel() as channel:
        yield channel


@fixture(scope="module")
def grpc_stub_cls(grpc_channel: Channel) -> type[MineStub]:
    return MineStub


@fixture(scope="module")
async def grpc_aio_stub(
    grpc_stub_cls: type[AsyncMineStub], grpc_aio_channel: Channel
) -> AsyncGenerator[AsyncMineStub, None]:
    yield grpc_stub_cls(grpc_aio_channel)
