import re

from mine.pb2 import CountRequest, FizzBuzzRequest, MineStub


def test_fizzbuzz(grpc_stub: MineStub) -> None:
    for i in range(100):
        request = FizzBuzzRequest(i=i)
        response = grpc_stub.FizzBuzz(request)
        matched = re.match(r"^(Fizz)?(Buzz)?$", response.s)
        assert matched is not None
        fizz, buzz = matched.groups()
        assert (fizz is not None) == (i % 3 == 0)
        assert (buzz is not None) == (i % 5 == 0)


def test_count(grpc_stub: MineStub) -> None:
    n = 3
    request = CountRequest(n=n)
    responses = list(grpc_stub.Count(request))
    assert [r.i for r in responses] == list(range(n))
