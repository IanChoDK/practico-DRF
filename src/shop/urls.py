from django.urls import path

from .views import RopaListCreateAPIView, RopaDetailAPIView, CategoriaListCreateAPIView, CategoriaDetailAPIView, ProveedorListCreateAPIView, ProveedorDetailAPIView

urlpatterns = [
    path("ropa", RopaListCreateAPIView.as_view(), name="ropa_api"),
    path("ropa/<int:pk>/", RopaDetailAPIView.as_view(), name="ropa_detail_api"),
    path("categorias", CategoriaListCreateAPIView.as_view(), name="categorias_api"),
    path("categorias/<int:pk>/", CategoriaDetailAPIView.as_view(), name="categoria_detail_api"),
    path("proveedores", ProveedorListCreateAPIView.as_view(), name="proveedores_api"),
    path("proveedores/<int:pk>/", ProveedorDetailAPIView.as_view(), name="proveedor_detail_api"),
]