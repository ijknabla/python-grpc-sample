import asyncio
from collections.abc import Callable, Coroutine
from functools import wraps
from typing import Any, ParamSpec, TypeVar

_P = ParamSpec("_P")
_T = TypeVar("_T")


def run(f: Callable[_P, Coroutine[Any, Any, _T]]) -> Callable[_P, _T]:
    @wraps(f)
    def wrapped(*args: _P.args, **kwargs: _P.kwargs) -> _T:
        return asyncio.run(f(*args, **kwargs))

    return wrapped
