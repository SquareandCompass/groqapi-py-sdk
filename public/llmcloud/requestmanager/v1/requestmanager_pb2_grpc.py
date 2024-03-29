# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from public.llmcloud.requestmanager.v1 import (
    requestmanager_pb2 as public_dot_llmcloud_dot_requestmanager_dot_v1_dot_requestmanager__pb2,
)


class RequestManagerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTextCompletionStream = channel.unary_stream(
            "/public.llmcloud.requestmanager.v1.RequestManagerService/GetTextCompletionStream",
            request_serializer=public_dot_llmcloud_dot_requestmanager_dot_v1_dot_requestmanager__pb2.GetTextCompletionRequest.SerializeToString,
            response_deserializer=public_dot_llmcloud_dot_requestmanager_dot_v1_dot_requestmanager__pb2.GetTextCompletionStreamResponse.FromString,
        )
        self.GetTextCompletion = channel.unary_unary(
            "/public.llmcloud.requestmanager.v1.RequestManagerService/GetTextCompletion",
            request_serializer=public_dot_llmcloud_dot_requestmanager_dot_v1_dot_requestmanager__pb2.GetTextCompletionRequest.SerializeToString,
            response_deserializer=public_dot_llmcloud_dot_requestmanager_dot_v1_dot_requestmanager__pb2.GetTextCompletionResponse.FromString,
        )


class RequestManagerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetTextCompletionStream(self, request, context):
        """completes text based on query and get back a stream of tokens
        buf:lint:ignore RPC_REQUEST_STANDARD_NAME
        buf:lint:ignore RPC_REQUEST_RESPONSE_UNIQUE
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetTextCompletion(self, request, context):
        """completes text based on query and get back a message with the full response
        buf:lint:ignore RPC_REQUEST_RESPONSE_UNIQUE
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_RequestManagerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetTextCompletionStream": grpc.unary_stream_rpc_method_handler(
            servicer.GetTextCompletionStream,
            request_deserializer=public_dot_llmcloud_dot_requestmanager_dot_v1_dot_requestmanager__pb2.GetTextCompletionRequest.FromString,
            response_serializer=public_dot_llmcloud_dot_requestmanager_dot_v1_dot_requestmanager__pb2.GetTextCompletionStreamResponse.SerializeToString,
        ),
        "GetTextCompletion": grpc.unary_unary_rpc_method_handler(
            servicer.GetTextCompletion,
            request_deserializer=public_dot_llmcloud_dot_requestmanager_dot_v1_dot_requestmanager__pb2.GetTextCompletionRequest.FromString,
            response_serializer=public_dot_llmcloud_dot_requestmanager_dot_v1_dot_requestmanager__pb2.GetTextCompletionResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "public.llmcloud.requestmanager.v1.RequestManagerService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class RequestManagerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetTextCompletionStream(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_stream(
            request,
            target,
            "/public.llmcloud.requestmanager.v1.RequestManagerService/GetTextCompletionStream",
            public_dot_llmcloud_dot_requestmanager_dot_v1_dot_requestmanager__pb2.GetTextCompletionRequest.SerializeToString,
            public_dot_llmcloud_dot_requestmanager_dot_v1_dot_requestmanager__pb2.GetTextCompletionStreamResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetTextCompletion(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/public.llmcloud.requestmanager.v1.RequestManagerService/GetTextCompletion",
            public_dot_llmcloud_dot_requestmanager_dot_v1_dot_requestmanager__pb2.GetTextCompletionRequest.SerializeToString,
            public_dot_llmcloud_dot_requestmanager_dot_v1_dot_requestmanager__pb2.GetTextCompletionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
