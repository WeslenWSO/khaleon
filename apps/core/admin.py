from django.contrib import admin

from apps.core.models import SiteConfig, Stat, TeamMember, Testimonial, Partner


@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Identidade", {"fields": ("site_name", "tagline", "meta_description")}),
        ("Hero", {"fields": ("hero_title", "hero_subtitle", "hero_cta_text", "hero_cta_url")}),
        ("Sobre", {"fields": ("about_title", "about_intro", "mission", "vision", "values")}),
        ("Contato", {"fields": ("phone", "email", "whatsapp", "address", "map_embed")}),
        ("Redes sociais", {"fields": ("linkedin", "instagram", "facebook")}),
        ("Acesso ao sistema", {"fields": ("system_active", "system_title", "system_description", "system_url")}),
    )

    def has_add_permission(self, request):
        return not SiteConfig.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ("value", "label", "order")
    list_editable = ("order",)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "company", "active", "order")
    list_filter = ("active",)
    list_editable = ("active", "order")
    search_fields = ("name", "company")


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "active", "order")
    list_filter = ("active",)
    list_editable = ("active", "order")
    search_fields = ("name", "role")


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "active", "order")
    list_filter = ("active",)
    list_editable = ("active", "order")
    search_fields = ("name", "url")
