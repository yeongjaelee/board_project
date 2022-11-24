# Create your views here.
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from board.models import PostDetail
from board.models.post import Post


def index(request):
    posts = Post.objects.all()
    post_all = {"posts": posts}
    page = request.GET.get('page', '1')
    paginator = Paginator(posts, '5')
    page_obj = paginator.page(page)
    return render(request, './post_list.html', {'page_obj': page_obj})


def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        post=Post.objects.create(title=title)
        PostDetail.objects.create(post=post, context=content)

    return render(request, './create_new.html')


def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    print(post)
    post_detail = post.details.all()
    print(post_detail)
    return render(request, './post_detail.html', {'post_detail': post_detail})


