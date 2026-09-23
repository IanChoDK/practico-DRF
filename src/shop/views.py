from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Ropa, Categoria, Proveedor, Color, Talle
from .serializers import RopaSerializer, RopaPublicSerializer, CategoriaSerializer,ProveedorSerializer, ColorSerializer, TalleSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# List -> Get all  
# Create -> Post
# Retrieve -> Get by id/pk
# Update -> Put
# destroy -> Delete

# Create your views here.

class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ColorSerializer

class TalleViewSet(viewsets.ModelViewSet):
    queryset = Talle.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = TalleSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategoriaSerializer


class RopaViewSet(viewsets.ModelViewSet):
    queryset = Ropa.objects.all()
    permission_clases = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return RopaPublicSerializer
        else:
            return RopaSerializer
    

class ProveedorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    permission_clases = [IsAuthenticated]

    @action(detail=True, methods=["delete"])
    def logico(self, request, pk=None):
        proveedor = self.get_object()
        proveedor.activo = False
        proveedor.save()
        return Response({"status":"El proveedor esta inactivo."})

