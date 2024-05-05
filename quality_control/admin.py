from django.contrib import admin

# Register your models here.
from .models import BugReport, FeatureRequest

@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'status', 'updated_at', 'project', 'task')
    list_filter = ('created_at', 'priority', 'status')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'status', 'updated_at', 'project', 'task')
    list_filter = ('created_at', 'priority', 'status')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')

