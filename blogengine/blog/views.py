from django.shortcuts import render, redirect
from django.views.generic import View
from .utils import *

from .models import Post, Tag
from .forms import TagForm, PostForm


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


class TagCreate(ObjectCreateMixin, View):
    model_form = TagForm
    template = 'blog/tag_create.html'


class TagUpdate(View):
    def get(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        bound_form = TagForm(instance=tag)
        return render(request, 'blog/tag_update_form.html', context={'form': bound_form, 'tag': tag})


class PostCreate(ObjectCreateMixin, View):
    model_form = PostForm
    template = 'blog/post_create_form.html'
