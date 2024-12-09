from django.contrib import admin
from .models import ContactMessage, SiteStatistics

# Register your models here.

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)

class SiteStatisticsAdmin(admin.ModelAdmin):
    list_display = ('site_visits', 'game_downloads', 'last_updated')
    readonly_fields = ('site_visits', 'game_downloads', 'last_updated')

admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(SiteStatistics, SiteStatisticsAdmin)
