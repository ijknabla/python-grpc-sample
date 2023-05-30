from collections.abc import AsyncIterable, Awaitable
from typing import Protocol

from mine import CountRequest, CountResponse, FizzBuzzRequest, FizzBuzzResponse


class SupportsMineStub(Protocol):
    def FizzBuzz(self, request: FizzBuzzRequest) -> Awaitable[FizzBuzzResponse]:
        ...

    def Count(self, request: CountRequest) -> AsyncIterable[CountResponse]:
        ...
