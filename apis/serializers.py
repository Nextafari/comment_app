from rest_framework import serializers
from .models import Comment, Like, Dislike, Reply


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = (
            "name",
            "email",
            "body"
        )


class GetReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = (
            "name",
            "email",
            "body",
            "date"
        )


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


class DisLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislike
        fields = "__all__"
