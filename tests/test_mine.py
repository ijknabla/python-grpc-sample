import re

import pytest

from mine import CountRequest, FizzBuzzRequest

from . import SupportsMineStub


@pytest.mark.asyncio
async def test_fizzbuzz(grpc_stub: SupportsMineStub) -> None:
    await _test_any_fizzbuzz(grpc_stub)


@pytest.mark.asyncio
async def test_async_fizzbuzz(grpc_aio_stub: SupportsMineStub) -> None:
    await _test_any_fizzbuzz(grpc_aio_stub)


async def _test_any_fizzbuzz(stub: SupportsMineStub) -> None:
    for i in range(100):
        request = FizzBuzzRequest(i=i)
        response = await stub.FizzBuzz(request)
        matched = re.match(r"^(Fizz)?(Buzz)?$", response.s)
        assert matched is not None
        fizz, buzz = matched.groups()
        assert (fizz is not None) == (i % 3 == 0)
        assert (buzz is not None) == (i % 5 == 0)


@pytest.mark.asyncio
async def test_count(grpc_stub: SupportsMineStub) -> None:
    await _test_any_count(grpc_stub)


@pytest.mark.asyncio
async def test_async_count(grpc_aio_stub: SupportsMineStub) -> None:
    await _test_any_count(grpc_aio_stub)


async def _test_any_count(stub: SupportsMineStub) -> None:
    n = 3
    request = CountRequest(n=n)
    responses = [r async for r in stub.Count(request)]
    assert [r.i for r in responses] == list(range(n))
