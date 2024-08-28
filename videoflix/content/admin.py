from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Video

# Register your models here.
# @admin.register(Video)
# class VideoAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description', 'created_at')
#     search_fields = ('title',)
# admin.site.register(Video)

class VideoResource(resources.ModelResource):
    class Meta:
        model = Video

@admin.register(Video)
class VideoAdmin(ImportExportModelAdmin):
    pass
# admin.site.register(VideoAdmin)