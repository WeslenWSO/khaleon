from django.contrib import admin

from apps.services.models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "icon", "order", "active")
    list_filter = ("active",)
    list_editable = ("order", "active")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "summary")
