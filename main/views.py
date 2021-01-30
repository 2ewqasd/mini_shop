from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import ImageForMain, EditMain, Products, Extra_Text

class ShowInformation(ListView):
    """A page representing a list of objects."""

    model = ImageForMain

    def get_context_data(self, **kwargs):
        """ Take objects and show them"""
        context = super().get_context_data(**kwargs)
        context["editmain"] = EditMain.objects.all()
        context["imageformain"] = ImageForMain.objects.all()
        context["products"] = Products.objects.all()
        context["extra_text"] = Extra_Text.objects.all()
        return context

class Goods(DetailView):

    model = Products
    slug_field = 'url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    
    