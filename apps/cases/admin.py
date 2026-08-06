from django.contrib import admin

from apps.cases.models import CaseStudy


@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    list_display = ("title", "client", "sector", "featured", "published")
    list_filter = ("sector", "featured", "published")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "client")
    fieldsets = (
        (None, {"fields": ("title", "slug", "sector", "client", "image")}),
        ("Conteúdo", {"fields": ("challenge", "solution", "results")}),
        ("Publicação", {"fields": ("featured", "published")}),
    )
