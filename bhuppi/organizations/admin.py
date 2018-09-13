from django.contrib import admin
from .models import Organization

class OrganizationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Organization._meta.get_fields()]

admin.site.register(Organization, OrganizationAdmin)
