from django.urls import path

from .views import ropa_list, ropa_detail, categorias_list, categoria_detail, proveedores_list, proveedor_detail

urlpatterns = [
    path("ropa", ropa_list, name="ropa_api"),
    path("ropa/<int:pk>/", ropa_detail, name="ropa_detail_api"),
    path("categorias", categorias_list, name="categorias_api"),
    path("categorias/<int:pk>/", categoria_detail, name="categoria_detail_api"),
    path("proveedores", proveedores_list, name="proveedores_api"),
    path("proveedores/<int:pk>/", proveedor_detail, name="proveedor_detail_api"),
]