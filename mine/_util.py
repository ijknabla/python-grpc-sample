import sys
from collections.abc import Generator
from contextlib import contextmanager

from pkg_resources import resource_filename


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
