from collections.abc import AsyncIterable, Awaitable
from typing import Protocol

from mine import FizzBuzzRequest, FizzBuzzResponse, UnsignedInteger


class SupportsMineStub(Protocol):
    def FizzBuzz(self, request: FizzBuzzRequest) -> Awaitable[FizzBuzzResponse]:
        ...

    def Count(self, request: UnsignedInteger) -> AsyncIterable[UnsignedInteger]:
        ...
