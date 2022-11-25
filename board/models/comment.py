from django.db import models

from board.models import PostDetail


class Comment(models.Model):
    post_detail = models.ForeignKey(PostDetail, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
