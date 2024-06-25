from django.contrib import admin
from .models import Contact


class ContactFormAdmin(admin.ModelAdmin):
    readonly_fields = (
        'contact_name',
        'contact_email',
        'contact_message',
        'contact_date',
    )

    fields = (
        'contact_name',
        'contact_email',
        'contact_date',
        'contact_message',
    )

    list_display = (
        'contact_name',
        'contact_email',
        'contact_date',
    )

    ordering = ('-contact_date',)


admin.site.register(Contact, ContactFormAdmin)
