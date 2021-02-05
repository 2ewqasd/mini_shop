from django.urls import path
from .views import Goods, ShowInformation

urlpatterns = [
    path("", ShowInformation.as_view(template_name="index.html"), name="main"),
    path("good/<slug:slug>", Goods.as_view(template_name="product.html"), name="product"),
]
