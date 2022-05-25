from __future__ import annotations

from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

from .models import Post


def post_list(request: HttpRequest) -> HttpResponse:
    """Returns list of all posts."""
    
    posts=Post.objects.filter(status='published')

    context = {
        "posts": posts
    }

    return render(request, "post_list.html", context)


def post_detail(request: HttpRequest, slug:str) -> HttpResponse:
    """Returns post detail page."""
    try:
        post=Post.objects.filter(slug=slug).first()
        post.update(page_views=F("page_views") + 1)
    except Post.DoesNotExist:
        return HttpResponseNotFound(_("This element does not exist."))

    context = {
        "post": post,
    }

    return render(request, "post_detail.html", context)