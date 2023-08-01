from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ("Name","Email","Phone_no")


admin.site.register(Contact, ContactAdmin)
