from django.contrib import admin

from apps.contact.models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "company", "created_at", "read")
    list_filter = ("read", "created_at")
    search_fields = ("name", "email", "company", "message")
    readonly_fields = ("name", "email", "phone", "company", "message", "created_at")
    list_editable = ("read",)

    def has_add_permission(self, request):
        return False
