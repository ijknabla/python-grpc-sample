from abc import ABCMeta as _ABCMeta
from collections.abc import Iterator as _Iterator
from typing import TypeVar as _TypeVar

import grpc

_T = _TypeVar("_T")

class _Rendezvous(_Iterator[_T], grpc.RpcError, grpc.RpcContext, metaclass=_ABCMeta): ...
class _MultiThreadedRendezvous(_Rendezvous[_T], grpc.Call, grpc.Future, metaclass=_ABCMeta): ...
