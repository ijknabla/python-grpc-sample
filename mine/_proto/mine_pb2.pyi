from dataclasses import dataclass as _dataclass
from dataclasses import field as _field

@_dataclass
class UnsignedInteger:
    u: int = _field(default=int())

@_dataclass
class FizzBuzzRequest:
    i: int = _field(default=int())

@_dataclass
class FizzBuzzResponse:
    s: str = _field(default=str())
