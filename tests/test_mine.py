import re
from collections.abc import AsyncIterator

import pytest

from mine import FizzBuzzRequest, SupportsAsyncMineStub, UnsignedInteger


@pytest.mark.asyncio
async def test_fizzbuzz(grpc_stub: SupportsAsyncMineStub) -> None:
    await _test_any_fizzbuzz(grpc_stub)


@pytest.mark.asyncio
async def test_async_fizzbuzz(grpc_aio_stub: SupportsAsyncMineStub) -> None:
    await _test_any_fizzbuzz(grpc_aio_stub)


async def _test_any_fizzbuzz(stub: SupportsAsyncMineStub) -> None:
    for i in range(100):
        request = FizzBuzzRequest(i=i)
        response = await stub.FizzBuzz(request)
        matched = re.match(r"^(Fizz)?(Buzz)?$", response.s)
        assert matched is not None
        fizz, buzz = matched.groups()
        assert (fizz is not None) == (i % 3 == 0)
        assert (buzz is not None) == (i % 5 == 0)


@pytest.mark.asyncio
async def test_count(grpc_stub: SupportsAsyncMineStub) -> None:
    await _test_any_count(grpc_stub)


@pytest.mark.asyncio
async def test_async_count(grpc_aio_stub: SupportsAsyncMineStub) -> None:
    await _test_any_count(grpc_aio_stub)


async def _test_any_count(stub: SupportsAsyncMineStub) -> None:
    u = 3
    request = UnsignedInteger(u=u)
    responses = [r async for r in stub.Count(request)]
    assert [r.u for r in responses] == list(range(u))


@pytest.mark.asyncio
async def test_sum(grpc_stub: SupportsAsyncMineStub) -> None:
    await _test_any_sum(grpc_stub)


@pytest.mark.asyncio
async def test_async_sum(grpc_aio_stub: SupportsAsyncMineStub) -> None:
    await _test_any_sum(grpc_aio_stub)


async def _test_any_sum(stub: SupportsAsyncMineStub) -> None:
    us = range(100)

    async def values_iterator() -> AsyncIterator[UnsignedInteger]:
        for u in us:
            yield UnsignedInteger(u=u)

    response = await stub.Sum(values_iterator())
    assert sum(us) == response.u
