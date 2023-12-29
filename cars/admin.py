from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40px" style="border-radius:10px;" />'.format(object.car_photo.url))
    thumbnail.short_description="Photo"
    list_display=('id','thumbnail','city','car_title','color','model','year','body_style','fuel_type','is_featured')
    list_display_links=('id','car_title','thumbnail')
    list_editable=('is_featured',)
    search_fields=('id','car_title','color','model','body_style','fuel_type',)
    list_filter=('city','car_title','color','fuel_type',)

admin.site.register(Car,CarAdmin)