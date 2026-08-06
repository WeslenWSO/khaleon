from django.shortcuts import render

from apps.blog.models import Post
from apps.core.models import SiteConfig, Stat
from apps.services.models import Service


def home(request):
    config = SiteConfig.load()
    context = {
        "config": config,
        "services": Service.objects.filter(active=True)[:6],
        "stats": Stat.objects.all(),
        "posts": Post.objects.filter(published=True)[:6],
        "page_title": config.site_name,
        "meta_description": config.meta_description or config.tagline,
    }
    return render(request, "pages/core/home.html", context)


def about(request):
    config = SiteConfig.load()
    context = {
        "config": config,
        "stats": Stat.objects.all(),
        "page_title": f"Sobre — {config.site_name}",
        "meta_description": config.about_intro[:160] if config.about_intro else config.meta_description,
    }
    return render(request, "pages/core/about.html", context)
