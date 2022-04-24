import os
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.views import APIView
from rest_framework import status
from .models import Comment, Reply
from rest_framework.response import Response
from .pagination import CustomPagination
from .serializers import (
    CommentSerializer,
    LikeSerializer,
    DisLikeSerializer,
    ReplySerializer,
    GetReplySerializer,
)
from django.core.mail import send_mail
from django.conf import settings
from comment_api.utils import convert_to_random_days


class PostComment(CreateAPIView):
    """Sends the Comment to the DB"""
    serializer_class = CommentSerializer

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data.get("name")
        email = serializer.validated_data.get("email")
        body = serializer.validated_data.get("body")
        recipient = os.environ["RECIPIENT"]

        send_mail(
            f"Comment From {name} & {email} on your Page",
            body,
            settings.EMAIL_HOST_USER,
            [recipient],
            fail_silently=False,
        )

        # serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


class PostReply(CreateAPIView):
    """Sends the Reply to the DB"""
    serializer_class = ReplySerializer

    def post(self, request, pk):
        serializer = ReplySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data.get("name")
        email = serializer.validated_data.get("email")
        body = serializer.validated_data.get("body")
        comment = Comment.objects.get(pk=pk)
        Reply.objects.create(
            name=name,
            email=email,
            body=body,
            comment=comment,
            date=convert_to_random_days
        )
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


class GetReply(APIView):
    """Gets replies from DB"""
    serializer_class = ReplySerializer

    def get(self, request, pk):
        replies = Reply.objects.filter(comment=pk)
        serializer = GetReplySerializer(replies, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class GetComment(GenericAPIView):
    """Gets comment from DB"""
    queryset = Comment.objects.all().order_by("-body")
    serializer_class = CommentSerializer
    pagination_class = CustomPagination

    def get(self, request):
        queryset = self.get_queryset()
        # page = self.request.query_params.get('page')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.serializer_class(page, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class LikeComment(CreateAPIView):
    """Sends the Likes to the DB"""
    serializer_class = LikeSerializer

    def post(self, request):
        serializer = LikeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


class DislikeComment(CreateAPIView):
    """Sends the Dislikes to the DB"""
    serializer_class = DisLikeSerializer

    def post(self, request):
        serializer = DisLikeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
