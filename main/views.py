from django.shortcuts import render
from django.views.generic.list import ListView
from .models import ImageForMain, EditMain

class ShowInformation(ListView):
    """A page representing a list of objects."""

    model = ImageForMain

    def get_context_data(self, **kwargs):
        """ Take objects and show them"""
        context = super().get_context_data(**kwargs)
        context["editmain"] = EditMain.objects.all()
        return context

    
    