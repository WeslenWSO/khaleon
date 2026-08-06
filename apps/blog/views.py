from django.core.paginator import Paginator
from django.db import OperationalError, ProgrammingError
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from apps.blog.models import Category, Post
from apps.core.db_utils import safe_query


def post_list(request):
    try:
        posts = Post.objects.filter(published=True)
        categories = list(Category.objects.all())
        category_slug = request.GET.get("categoria")
        category = None

        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            posts = posts.filter(category=category)
    except (OperationalError, ProgrammingError):
        posts = Post.objects.none()
        categories = []
        category = None

    paginator = Paginator(posts, 6)
    page = paginator.get_page(request.GET.get("page"))

    context = {
        "page_obj": page,
        "categories": categories,
        "current_category": category,
        "page_title": "Blog — Khaleon IA",
        "meta_description": "Artigos sobre BPO, automação, inteligência artificial e transformação digital.",
    }
    return render(request, "pages/blog/list.html", context)


def post_detail(request, slug):
    try:
        post = get_object_or_404(Post, slug=slug, published=True)
    except (OperationalError, ProgrammingError):
        raise Http404("Artigo não encontrado") from None

    context = {
        "post": post,
        "page_title": post.seo_title,
        "meta_description": post.seo_description,
    }
    return render(request, "pages/blog/detail.html", context)
