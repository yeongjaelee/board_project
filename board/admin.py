from django.contrib import admin

from board.models import PostDetail, Comment
from board.models.post import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(PostDetail)
class PostDetail(admin.ModelAdmin):
    pass

@admin.register(Comment)
class Comment(admin.ModelAdmin):
    pass