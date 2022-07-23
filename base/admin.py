from django.contrib import admin

# Register your models here.

from .models import about, mySkill, service, contact

admin.site.register(about)
admin.site.register(mySkill)
admin.site.register(service)
admin.site.register(contact)