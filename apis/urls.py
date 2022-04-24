from django.urls import path
from . import views

urlpatterns = [
    path(
        'post-comment',
        views.PostComment.as_view(),
        name="post_comment"
    ),
    path(
        'like-comment',
        views.LikeComment.as_view(),
        name="like_comment"
    ),
    path(
        'get-comment',
        views.GetComment.as_view(),
        name="get_comment"
    ),
    path(
        'dislike-comment',
        views.DislikeComment.as_view(),
        name="dislike_comment"
    ),
    path(
        'reply-comment/<int:pk>/',
        views.PostReply.as_view(),
        name="reply_comment"
    ),
    path(
        'replies/<int:pk>',
        views.GetReply.as_view(),
        name='replies'
    )
]
