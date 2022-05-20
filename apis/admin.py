from django.contrib import admin
from .models import Comment, Like, Dislike, Reply


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'body',
        'date',
    )


admin.site.register(Comment, CommentAdmin)


class ReplyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'body',
        'date',
    )


admin.site.register(Reply, ReplyAdmin)


# class LikeAdmin(admin.ModelAdmin):
#     list_display = (
#         'comment',
#         'like',
#     )


# admin.site.register(Like, LikeAdmin)


# class DisLikeAdmin(admin.ModelAdmin):
#     list_display = (
#         'comment',
#         'dislike',
#     )


# admin.site.register(Dislike, DisLikeAdmin)
