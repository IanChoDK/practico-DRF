from django.urls import path

from .views import ropa_list, ropa_detail

urlpatterns = [
    path("", ropa_list, name="ropa_api"),
    path("<int:pk>/", ropa_detail, name="ropa_detail_api")
]