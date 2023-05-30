import re
from collections.abc import AsyncIterable, AsyncIterator, Awaitable, Iterable
from typing import TypeVar

import pytest

from mine import (
    AsyncMineStub,
    CountRequest,
    CountResponse,
    FizzBuzzRequest,
    FizzBuzzResponse,
    MineStub,
)

AnyMineStub = MineStub | AsyncMineStub
T = TypeVar("T")


@pytest.mark.asyncio
async def test_fizzbuzz(grpc_stub: MineStub) -> None:
    await _test_any_fizzbuzz(grpc_stub)


@pytest.mark.asyncio
async def test_async_fizzbuzz(grpc_aio_stub: AsyncMineStub) -> None:
    await _test_any_fizzbuzz(grpc_aio_stub)


async def _test_any_fizzbuzz(stub: AnyMineStub) -> None:
    for i in range(100):
        request = FizzBuzzRequest(i=i)
        response = await _call_fizzbuzz(stub, request)
        matched = re.match(r"^(Fizz)?(Buzz)?$", response.s)
        assert matched is not None
        fizz, buzz = matched.groups()
        assert (fizz is not None) == (i % 3 == 0)
        assert (buzz is not None) == (i % 5 == 0)


async def _call_fizzbuzz(stub: AnyMineStub, request: FizzBuzzRequest) -> FizzBuzzResponse:
    response = stub.FizzBuzz(request)
    if isinstance(response, Awaitable):
        return await response
    else:
        return response


@pytest.mark.asyncio
async def test_count(grpc_stub: MineStub) -> None:
    await _test_any_count(grpc_stub)


@pytest.mark.asyncio
async def test_async_count(grpc_aio_stub: MineStub) -> None:
    await _test_any_count(grpc_aio_stub)


async def _test_any_count(stub: AnyMineStub) -> None:
    n = 3
    request = CountRequest(n=n)
    responses = [r async for r in _call_count(stub, request)]
    assert [r.i for r in responses] == list(range(n))


def _call_count(stub: AnyMineStub, request: CountRequest) -> AsyncIterable[CountResponse]:
    responses = stub.Count(request)
    if isinstance(responses, AsyncIterable):
        return responses
    else:
        return _iter_async(responses)


async def _iter_async(iterable: Iterable[T]) -> AsyncIterator[T]:
    for item in iterable:
        yield item
