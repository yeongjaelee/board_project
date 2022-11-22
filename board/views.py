# Create your views here.
from django.shortcuts import render, redirect

from board.models import PostDetail
from board.models.post import Post


def index(request):
    posts = Post.objects.all()
    post_all = {"posts": posts}
    return render(request, './post_list.html', post_all)


def create(request):
    if request.method == "POST":
        print(1)
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(title=title)
        PostDetail.objects.create(context=content)
    return render(request, './post_detail.html')

