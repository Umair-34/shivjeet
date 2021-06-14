from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
# Apply summernote to all TextField in model.

@admin.action(description='Mark selected Properties as approved')
def make_approved(modeladmin, request, queryset):
    queryset.update(Status=True)


@admin.action(description='Mark selected Properties as unapproved')
def make_unapproved(modeladmin, request, queryset):
    queryset.update(Status=False)


@admin.action(description='Mark selected properties featured')
def make_featured(modeladmin, request, queryset):
    queryset.update(Featured=True)


class PropertyAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = 'Description'
    search_fields = ('City__Name', 'Region__Name', 'Name')
    list_display = ('City', 'Address', 'created_on', 'Status', 'Featured')
    list_filter = ('Status', 'City__Name', 'Region__Name', 'created_on')
    actions = [make_approved, make_unapproved, make_featured]


admin.site.register(Property, PropertyAdmin)
admin.site.register(City)
admin.site.register(Region)
admin.site.register(Amenities)
admin.site.register(PropertyType)
admin.site.register(SubPropertyType)
admin.site.register(AreaUnit)