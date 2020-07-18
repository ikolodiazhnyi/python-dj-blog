from django.shortcuts import render

from .models import Post


def posts_list(request):
    posts_all = Post.objects.all()

    return render(request, 'blog/index.html', context={'posts': posts_all})


def post_detail(request, slug):
    post_details = Post.objects.get(slug__iexact=slug)

    return render(request, 'blog/post_detail.html', context={'post': post_details})
