from django.contrib import admin
from . models import (Priority,Category)


@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = (
        'id', 'name', 'code', 'is_active', 'created_at', 'updated_at',
    )
    list_display_links = ('name',)
    list_filter = ('created_at',)
    search_fields = ['name', 'code']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = (
        'id', 'title', 'slug', 'is_active', 'created_at', 'updated_at',
    )

