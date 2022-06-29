from django.contrib import admin
from cars.models import Car
from django.utils.html import format_html
# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display=("thumbnail","car_title","color","year","city","model","body_style","fuele_type",'is_featured')
    list_display_links=("thumbnail","car_title")
    search_fields=("car_title","color","year","city","model","body_style","fuele_type",'is_featured')
    list_filter=("is_featured",)
    list_editable=('is_featured',)
    def thumbnail(self,object):
        return format_html('<img src={}  width="40px" style="border-radius:50px;" />'.format(object.car_photo.url))
    thumbnail.short_description='photo'


admin.site.register(Car,CarAdmin)
