from django.contrib import admin

from contacts.models import Contact

class ContactAdmin(admin.ModelAdmin):

    list_display=('id','first_name','last_name','car_title','city','email','phone','create_date')
    list_display_links=('id','first_name','email','car_title')
    search_fields=('first_name','last_name','email','car_title')
    list_filter=('car_title',)
    list_per_page=25

# Register your models here.
admin.site.register(Contact,ContactAdmin)
