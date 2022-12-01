# Create your views here.
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from board.models import PostDetail, Comment
from board.models.post import Post


def index(request, **kwargs):
    #delete post
    delete_post_id = kwargs.get('delete_post_id')
    if delete_post_id:
        delete_post = Post.objects.get(pk=delete_post_id)
        delete_post.delete()
    posts = Post.objects.all()
    page = request.GET.get('page', '1')
    paginator = Paginator(posts, '5')
    page_obj = paginator.page(page)
    return render(request, './post_list.html', {'page_obj': page_obj})


def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(title=title)
        PostDetail.objects.create(post=post, context=content)
    return render(request, './create_new.html')


def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    post_detail = PostDetail.objects.get(post=post)
    comment = ""
    if request.method == "POST":
        comment = request.POST.get('comment')
        title = request.POST.get('post_title')
        content = request.POST.get('post_detail_content')
        post.title = title
        post.save()
        post_detail.context = content
        post_detail.save()
    comment = comment
    if not comment == "":
        Comment.objects.create(post_detail=post_detail, comment=comment)
    comments = Comment.objects.filter(post_detail=post_detail)
    comment_count = comments.count()
    page = request.GET.get('page', '1')
    paginator = Paginator(comments, '3')
    page_comment = paginator.page(page)

    return render(request, './post_detail.html', {'post_detail': post_detail,
                                                  'page_comment': page_comment,
                                                  'comment_count': comment_count,
                                                  'post': post})


def update(request, **kwargs):
    print(1)
    print(post_id)
    post = Post.objects.get(pk=post_id)
    print(post)
    if request.method == "POST":
        print(000)
        title = request.POST.get('post_title')
        content = request.POST.get('post_detail_content')
        post.title = title
        post.save()
        print(111)
    print(222)
    return render(request, 'post_list.html')


