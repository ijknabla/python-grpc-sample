# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import mine_pb2 as mine__pb2


class MineStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.FizzBuzz = channel.unary_unary(
                '/Mine.Mine/FizzBuzz',
                request_serializer=mine__pb2.FizzBuzzRequest.SerializeToString,
                response_deserializer=mine__pb2.FizzBuzzResponse.FromString,
                )
        self.Count = channel.unary_stream(
                '/Mine.Mine/Count',
                request_serializer=mine__pb2.UnsignedInteger.SerializeToString,
                response_deserializer=mine__pb2.UnsignedInteger.FromString,
                )
        self.Sum = channel.stream_unary(
                '/Mine.Mine/Sum',
                request_serializer=mine__pb2.UnsignedInteger.SerializeToString,
                response_deserializer=mine__pb2.UnsignedInteger.FromString,
                )


class MineServicer(object):
    """Missing associated documentation comment in .proto file."""

    def FizzBuzz(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Count(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Sum(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MineServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'FizzBuzz': grpc.unary_unary_rpc_method_handler(
                    servicer.FizzBuzz,
                    request_deserializer=mine__pb2.FizzBuzzRequest.FromString,
                    response_serializer=mine__pb2.FizzBuzzResponse.SerializeToString,
            ),
            'Count': grpc.unary_stream_rpc_method_handler(
                    servicer.Count,
                    request_deserializer=mine__pb2.UnsignedInteger.FromString,
                    response_serializer=mine__pb2.UnsignedInteger.SerializeToString,
            ),
            'Sum': grpc.stream_unary_rpc_method_handler(
                    servicer.Sum,
                    request_deserializer=mine__pb2.UnsignedInteger.FromString,
                    response_serializer=mine__pb2.UnsignedInteger.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Mine.Mine', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Mine(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def FizzBuzz(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Mine.Mine/FizzBuzz',
            mine__pb2.FizzBuzzRequest.SerializeToString,
            mine__pb2.FizzBuzzResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Count(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Mine.Mine/Count',
            mine__pb2.UnsignedInteger.SerializeToString,
            mine__pb2.UnsignedInteger.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Sum(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/Mine.Mine/Sum',
            mine__pb2.UnsignedInteger.SerializeToString,
            mine__pb2.UnsignedInteger.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
