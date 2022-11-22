# Create your views here.
from django.shortcuts import render, redirect

from board.models import PostDetail
from board.models.post import Post


def index(request):
    print(1)
    posts = Post.objects.all()
    post_details = PostDetail.objects.all()
    post_all = {"posts": posts, "post_details_all": post_details}
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(title=title)
        PostDetail.objects.create(context=content)
    return render(request, './post_list.html', post_all)


