from django.contrib import admin
from .models import EditMain, ImageForMain, Products, Extra_Text, Extra_Text_Product

class TextMain(admin.StackedInline):
    model = Extra_Text
    extra = 1

class TextProduct(admin.StackedInline):
    model = Extra_Text_Product
    extra = 1

class TextP(admin.ModelAdmin):
    inlines = [TextProduct]
    list_display = ('title','pub_date',)

class Text(admin.ModelAdmin):
    inlines = [TextMain]


admin.site.register(EditMain, Text)
admin.site.register(ImageForMain)
admin.site.register(Products, TextP)