from django.urls import path
from .views import ShowInformation

urlpatterns = [
    path("", ShowInformation.as_view(template_name="index.html"), name="main"),
]