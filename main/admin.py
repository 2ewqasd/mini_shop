from django.contrib import admin
from .models import EditMain, ImageForMain, Products, Extra_Text

class TextMain(admin.StackedInline):
    model = Extra_Text
    extra = 1

class Text(admin.ModelAdmin):
    inlines = [TextMain]

class Time(admin.ModelAdmin):
    list_display = ('title','pub_date',)

admin.site.register(EditMain, Text)
admin.site.register(ImageForMain)
admin.site.register(Products, Time)