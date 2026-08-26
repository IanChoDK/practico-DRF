from django.urls import path

from .views import ropa_list

urlpatterns = [
    path("", ropa_list, name="ropa_api"),
]