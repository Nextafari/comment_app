from django.urls import path
from . import views

urlpatterns = [
    path(
        'post-comment',
        views.PostComment.as_view(),
        name="post_comment"
    ),
    path(
        'get-comment',
        views.GetComment.as_view(),
        name="get_comment"
    ),
    path(
        'comment-count',
        views.CountComment.as_view(),
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
