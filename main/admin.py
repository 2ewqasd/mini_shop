from django.contrib import admin
from .models import EditMain, ImageForMain

@admin.register(EditMain)
class QuillPostAdmin(admin.ModelAdmin):
    pass
admin.site.register(ImageForMain)