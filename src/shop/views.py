from rest_framework import generics

from .models import Ropa, Categoria, Proveedor
from .serializers import RopaSerializer, RopaPublicSerializer, CategoriaSerializer,ProveedorSerializer

# List -> Get all
# Create -> Post
# Retrieve -> Get by id/pk
# Update -> Put
# destroy -> Delete

# Create your views here.

class CategoriaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


    
class RopaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ropa.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return RopaPublicSerializer
        else:
            return RopaSerializer

class RopaDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ropa.objects.all()
    serializer_class = RopaSerializer



class ProveedorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class ProveedorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
