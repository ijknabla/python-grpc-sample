import re
from collections.abc import Awaitable

import pytest

from mine.pb2 import AsyncMineStub, CountRequest, FizzBuzzRequest, FizzBuzzResponse, MineStub

AnyMineStub = MineStub | AsyncMineStub


@pytest.mark.asyncio
async def test_fizzbuzz(grpc_stub: MineStub) -> None:
    await _test_any_fizzbuzz(grpc_stub)


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


def test_count(grpc_stub: MineStub) -> None:
    n = 3
    request = CountRequest(n=n)
    responses = list(grpc_stub.Count(request))
    assert [r.i for r in responses] == list(range(n))
