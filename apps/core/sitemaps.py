from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from apps.blog.models import Post
from apps.services.models import Service


class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return ["core:home", "core:about", "services:list", "blog:list", "contact:contact"]

    def location(self, item):
        return reverse(item)


class ServiceSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return Service.objects.filter(active=True)

    def lastmod(self, obj):
        return None


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return Post.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.updated_at
