from django.contrib import admin
from .models import Brand, Car, LeadRequest


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'price', 'condition', 'fuel', 'is_featured']
    list_filter  = ['brand', 'condition', 'fuel', 'body', 'is_featured']
    list_editable= ['is_featured']
    search_fields= ['brand__name', 'model']


@admin.register(LeadRequest)
class LeadRequestAdmin(admin.ModelAdmin):
    list_display  = ['name', 'phone', 'request_type', 'created_at', 'is_processed']
    list_filter   = ['request_type', 'is_processed']
    list_editable = ['is_processed']
    readonly_fields = ['created_at']