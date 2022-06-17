from django.contrib import admin
from pages.models import Team
from django.utils.html import format_html

class TeamAdmin(admin.ModelAdmin):
    list_display=("id","thumbnail","first_name","last_name","designation","create_date")
    list_display_links=("id","thumbnail","first_name")
    search_fields=("first_name","id","designation")
    list_filter=("designation",)
    def thumbnail(self,data):
        return format_html('<img src="{}" width="40" style="border-radius:50px;"/>'.format(data.image.url))

    thumbnail.short_description="photo"
# Register your models here.
admin.site.register(Team,TeamAdmin)
