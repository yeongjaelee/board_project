from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from board.models import Post


def post_list(request):
    title = {'board_title': 'this is for test'}
    return render(request, './post_list.html', title)

