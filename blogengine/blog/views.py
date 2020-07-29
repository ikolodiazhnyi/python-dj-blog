from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from .models import Post, Tag


def posts_list(request):
    posts_all = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts_all})


def tags_list(request):
    tags_all = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags_all})


class PostDetail(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug__iexact=slug)
        return render(request, 'blog/post_detail.html', context={'post': post})


class TagDetail(View):
    def get(self, request, slug):
        tag = get_object_or_404(Tag, slug__iexact=slug)
        return render(request, 'blog/tag_detail.html', context={'tag': tag})
