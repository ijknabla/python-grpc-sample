import asyncio
import sys
from collections.abc import Callable, Coroutine, Generator
from contextlib import contextmanager
from functools import wraps
from typing import Any, ParamSpec, TypeVar

from pkg_resources import resource_filename

_P = ParamSpec("_P")
_T = TypeVar("_T")


def run(f: Callable[_P, Coroutine[Any, Any, _T]]) -> Callable[_P, _T]:
    @wraps(f)
    def wrapped(*args: _P.args, **kwargs: _P.kwargs) -> _T:
        return asyncio.run(f(*args, **kwargs))

    return wrapped


@contextmanager
def push_module_to_path(module: str) -> Generator[None, None, None]:
    module = resource_filename(module, "")

    if module not in sys.path:
        sys.path.append(module)
        pushed = True
    else:
        pushed = False

    try:
        yield
    finally:
        if pushed:
            sys.path.remove(module)
