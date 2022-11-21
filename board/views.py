# Create your views here.
from django.shortcuts import render

from board.models import PostDetail
from board.models.post import Post


def index(request):
    posts = Post.objects.all()
    post_details = PostDetail.objects.all()
    post_all = {"posts": posts, "post_details_all": post_details}
    return render(request, './post_list.html', post_all)

