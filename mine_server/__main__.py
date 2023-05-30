from asyncio import run, sleep
from collections.abc import Callable, Coroutine
from functools import wraps
from typing import Any, ParamSpec, TypeVar

import click

from . import serve

_P = ParamSpec("_P")
_T = TypeVar("_T")


def run_main(f: Callable[_P, Coroutine[Any, Any, _T]]) -> Callable[_P, _T]:
    @wraps(f)
    def wrapped(*args: _P.args, **kwargs: _P.kwargs) -> _T:
        return run(f(*args, **kwargs))

    return wrapped


@click.command()
@click.option("--host", type=str, default="127.0.0.1")
@click.option("--port", type=int, required=True)
@run_main
async def main(
    host: str,
    port: int,
) -> None:
    with serve(host=host, port=port):
        while True:
            await sleep(1.0)


if __name__ == "__main__":
    main()
