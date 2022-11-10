from django.contrib import admin

from board.models import Post


@admin.register(Post)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)

