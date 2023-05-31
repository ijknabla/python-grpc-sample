from collections.abc import AsyncIterable, Awaitable, Iterable
from typing import TYPE_CHECKING, Generic, TypeVar

import grpc.aio

from . import _message as _

_Req0 = TypeVar("_Req0", contravariant=True)
_Req1 = TypeVar("_Req1", contravariant=True)
_Req2 = TypeVar("_Req2", contravariant=True)

_Res0 = TypeVar("_Res0", covariant=True)
_Res1 = TypeVar("_Res1", covariant=True)
_Res2 = TypeVar("_Res2", covariant=True)

_Ctx0 = TypeVar("_Ctx0", contravariant=True)
_Ctx1 = TypeVar("_Ctx1", contravariant=True)
_Ctx2 = TypeVar("_Ctx2", contravariant=True)


class _GenericMineStub(Generic[_Req0, _Res0, _Req1, _Res1, _Req2, _Res2]):
    if TYPE_CHECKING:

        def FizzBuzz(self, request: _Req0) -> _Res0:
            ...

        def Count(self, request: _Req1) -> _Res1:
            ...

        def Sum(self, request_iterator: _Req2) -> _Res2:
            ...


class _GenericMineServicer(Generic[_Req0, _Res0, _Ctx0, _Req1, _Res1, _Ctx1, _Req2, _Res2, _Ctx2]):
    if TYPE_CHECKING:

        def FizzBuzz(self, request: _Req0, context: _Ctx0) -> _Res0:
            ...

        def Count(self, request: _Req1, context: _Ctx1) -> _Res1:
            ...

        def Sum(self, request_iterator: _Req2, context: _Ctx2) -> _Res2:
            ...


SupportsDefaultMineStub = _GenericMineStub[
    _.FizzBuzzRequest,
    _.FizzBuzzResponse,
    _.CountRequest,
    Iterable[_.CountResponse],
    Iterable[_.SumRequest],
    _.SumResponse,
]

SupportsAsyncMineStub = _GenericMineStub[
    _.FizzBuzzRequest,
    Awaitable[_.FizzBuzzResponse],
    _.CountRequest,
    AsyncIterable[_.CountResponse],
    AsyncIterable[_.SumRequest],
    Awaitable[_.SumResponse],
]

SupportsDefaultMineServicer = _GenericMineServicer[
    _.FizzBuzzRequest,
    _.FizzBuzzResponse,
    grpc.ServicerContext,
    _.CountRequest,
    Iterable[_.CountResponse],
    grpc.ServicerContext,
    Iterable[_.SumRequest],
    _.SumResponse,
    grpc.ServicerContext,
]

SupportsAsyncMineServicer = _GenericMineServicer[
    _.FizzBuzzRequest,
    Awaitable[_.FizzBuzzResponse],
    grpc.aio.ServicerContext[
        _.FizzBuzzRequest,
        _.FizzBuzzResponse,
    ],
    _.CountRequest,
    AsyncIterable[_.CountResponse],
    grpc.aio.ServicerContext[
        _.CountRequest,
        _.CountResponse,
    ],
    AsyncIterable[_.SumRequest],
    Awaitable[_.SumResponse],
    grpc.aio.ServicerContext[
        _.SumRequest,
        _.SumResponse,
    ],
]
