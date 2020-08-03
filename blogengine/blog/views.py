from django.shortcuts import render
from django.views.generic import View
from .utils import ObjectDetailMixin

from .models import Post, Tag


def posts_list(request):
    posts_all = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts_all})


def tags_list(request):
    tags_all = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags_all})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'
