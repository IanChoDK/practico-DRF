from rest_framework.routers import DefaultRouter

from .views import RopaViewSet, CategoriaViewSet, ProveedorViewSet, ColorViewSet, TalleViewSet

router = DefaultRouter()

router.register("ropa", RopaViewSet, basename="ropa-api")
router.register("proveedor", ProveedorViewSet, basename="proveedor-api")
router.register("categoria", CategoriaViewSet, basename="categoria-api")
router.register("color", ColorViewSet, basename="color-api")
router.register("talle", TalleViewSet, basename="talle-api")