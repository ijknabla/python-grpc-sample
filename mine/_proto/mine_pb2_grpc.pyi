import grpc

from . import mine_pb2 as mine__pb2

class MineStub(object):
    def __init__(self, channel: grpc.Channel) -> None: ...
    def FizzBuzz(self, request: mine__pb2.FizzBuzzRequest) -> mine__pb2.FizzBuzzResponse: ...

class MineServicer(object):
    def FizzBuzz(
        self, request: mine__pb2.FizzBuzzRequest, context: grpc.ServicerContext
    ) -> mine__pb2.FizzBuzzResponse: ...

def add_MineServicer_to_server(servicer: MineServicer, server: grpc.Server) -> None: ...
