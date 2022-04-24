from django.db import models


class Comment(models.Model):
    name = models.CharField(max_length=150, blank=False)
    email = models.CharField(max_length=250, blank=False)
    body = models.TextField()
    date = models.CharField(max_length=40, default="1 day(s) ago")

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.name


class Reply(models.Model):
    name = models.CharField(max_length=150, blank=False)
    email = models.CharField(max_length=250, blank=False)
    body = models.TextField()
    comment = models.ForeignKey(
        Comment,
        related_name="comment_reply",
        null=True,
        on_delete=models.SET_NULL
    )
    date = models.CharField(max_length=40, default="1 day(s) ago")

    class Meta:
        verbose_name = "Reply"
        verbose_name_plural = "Replies"

    def __str__(self):
        return self.name


class Like(models.Model):
    like = models.BooleanField(default=False)
    comment = models.ForeignKey(Comment, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"

    def __str__(self):
        return self.name + self.like


class Dislike(models.Model):
    dislike = models.BooleanField(default=False)
    comment = models.ForeignKey(Comment, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Dislike"
        verbose_name_plural = "Dislikes"

    def __str__(self):
        return self.name + self.dislike
