from django.db import models

from board.models import Post


class PostDetail(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="details")
    context = models.TextField()
