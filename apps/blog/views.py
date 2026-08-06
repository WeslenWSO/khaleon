from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from apps.blog.models import Category, Post


def post_list(request):
    posts = Post.objects.filter(published=True)
    category_slug = request.GET.get("categoria")
    category = None

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=category)

    paginator = Paginator(posts, 6)
    page = paginator.get_page(request.GET.get("page"))

    context = {
        "page_obj": page,
        "categories": Category.objects.all(),
        "current_category": category,
        "page_title": "Blog — Khaleon IA",
        "meta_description": "Artigos sobre BPO, automação, inteligência artificial e transformação digital.",
    }
    return render(request, "pages/blog/list.html", context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    context = {
        "post": post,
        "page_title": post.seo_title,
        "meta_description": post.seo_description,
    }
    return render(request, "pages/blog/detail.html", context)
