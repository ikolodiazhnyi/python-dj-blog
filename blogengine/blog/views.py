from django.shortcuts import render

from .models import Post, Tag


def posts_list(request):
    posts_all = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts_all})


def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html', context={'post': post})


def tags_list(request):
    tags_all = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags_all})


def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'blog/tag_detail.html', context={'tag': tag})
