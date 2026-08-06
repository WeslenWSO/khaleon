from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.views.generic import TemplateView

from apps.core.sitemaps import PostSitemap, ServiceSitemap, StaticViewSitemap

sitemaps = {
    "static": StaticViewSitemap,
    "services": ServiceSitemap,
    "posts": PostSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.core.urls")),
    path("servicos/", include("apps.services.urls")),
    path("blog/", include("apps.blog.urls")),
    path("contato/", include("apps.contact.urls")),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
        name="robots",
    ),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Khaleon IA — Administração"
admin.site.site_title = "Khaleon IA"
admin.site.index_title = "Gerenciar conteúdo"
