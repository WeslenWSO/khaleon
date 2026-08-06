from django.contrib import admin

from apps.blog.models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "published", "published_at")
    list_filter = ("published", "category")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "excerpt")
    date_hierarchy = "published_at"
    fieldsets = (
        (None, {"fields": ("title", "slug", "category", "excerpt", "content", "image")}),
        ("Publicação", {"fields": ("published", "published_at")}),
        ("SEO", {"fields": ("meta_title", "meta_description")}),
    )
