from django.db import OperationalError, ProgrammingError
from django.http import JsonResponse
from django.shortcuts import render

from apps.blog.models import Post
from apps.core.context_processors import DEFAULT_SITE_CONFIG
from apps.core.models import SiteConfig, Stat
from apps.services.models import Service


def health(request):
    return JsonResponse({"status": "ok"})


def _load_config():
    try:
        return SiteConfig.load()
    except (OperationalError, ProgrammingError):
        return DEFAULT_SITE_CONFIG


def _safe_query(queryset_fn, fallback=None):
    try:
        return queryset_fn()
    except (OperationalError, ProgrammingError):
        return fallback if fallback is not None else []


def home(request):
    config = _load_config()
    context = {
        "config": config,
        "services": _safe_query(lambda: list(Service.objects.filter(active=True)[:6])),
        "stats": _safe_query(lambda: list(Stat.objects.all())),
        "posts": _safe_query(lambda: list(Post.objects.filter(published=True)[:6])),
        "page_title": config.site_name,
        "meta_description": config.meta_description or config.tagline,
    }
    return render(request, "pages/core/home.html", context)


def about(request):
    config = _load_config()
    context = {
        "config": config,
        "stats": _safe_query(lambda: list(Stat.objects.all())),
        "page_title": f"Sobre — {config.site_name}",
        "meta_description": config.about_intro[:160] if config.about_intro else config.meta_description,
    }
    return render(request, "pages/core/about.html", context)
