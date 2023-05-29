import re

from mine.rpc import MineStub
from mine.types import FizzBuzzRequest


def test_fizzbuzz(grpc_stub: MineStub) -> None:
    for i in range(100):
        request = FizzBuzzRequest(i=i)
        response = grpc_stub.FizzBuzz(request)
        matched = re.match(r"^(Fizz)?(Buzz)?$", response.s)
        assert matched is not None
        fizz, buzz = matched.groups()
        assert (fizz is not None) == (i % 3 == 0)
        assert (buzz is not None) == (i % 5 == 0)
