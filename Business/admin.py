from django.contrib import admin
from Business.models import BusinessGroup

class BusinessGroupAdmin(admin.ModelAdmin):
    filter_horizontal=('members', 'banned', 'subscribed',)

admin.site.register(BusinessGroup, BusinessGroupAdmin)
# Register your models here.
