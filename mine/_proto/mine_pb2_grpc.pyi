from typing import overload as _overload

import grpc.aio

from .. import _protocol

class MineStub(object): ...
class MineServicer(object): ...

@_overload
def add_MineServicer_to_server(
    servicer: _protocol.SupportsAsyncMineServicer, server: grpc.aio.Server
) -> None: ...
@_overload
def add_MineServicer_to_server(
    servicer: _protocol.SupportsDefaultMineServicer, server: grpc.Server
) -> None: ...
