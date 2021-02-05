from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import ImageForMain, EditMain, Products, Extra_Text
from .forms import ContactForm
from django.views.generic.edit import FormView
from django.core.mail import send_mail


class ShowInformation(ListView, FormView):
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

    template_name = 'index.html'
    form_class = ContactForm
    success_url = '/#'

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        send_mail('test1', f'{name} Test2', None, [email])
        return super().form_valid(form)


class Goods(DetailView):

    model = Products
    slug_field = 'url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
