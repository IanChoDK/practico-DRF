from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Ropa, Categoria, Proveedor
from .serializers import RopaSerializer, RopaPublicSerializer, CategoriaSerializer,ProveedorSerializer

# Create your views here.


@api_view(['GET','POST'])
def categorias_list(request):
    # Traer todas las categorias 
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Agregar una categoria
    if request.method == "POST":
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"mensaje": "Categoria creada"}, status=status.HTTP_201_CREATED
            )
        return Response(
            {"mensaje": "No se creó porque no es válido"},
            status=status.HTTP_400_BAD_REQUEST,
        )

@api_view(['GET','PUT','DELETE'])
def categoria_detail(request, pk):
    # Traer una sola categoria
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == "GET":
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Modificar una categoria
    if request.method == "PUT":
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"mensaje": "Categoria Actualizada"}, status=status.HTTP_200_OK
            )
        return Response(
            {"mensaje": "No se Actualizó porque no es válido"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Borrar categoria
    if request.method == "DELETE":
        categoria.delete()
        return Response(
            {"mensaje": "Categoria Borrada"},
            status=status.HTTP_200_OK,
        )
    

@api_view(['GET', 'POST'])
def ropa_list(request):
    # Traer toda la ropa
    if request.method == 'GET':
        ropa = Ropa.objects.all().select_related("proveedor","categoria","color")
        serializer = RopaPublicSerializer(ropa, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Agregar ropa
    if request.method == "POST":
        serializer = RopaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"mensaje": "Ropa creada"}, status=status.HTTP_201_CREATED
            )
        return Response(
            {"mensaje": "No se creó porque no es válido"},
            status=status.HTTP_400_BAD_REQUEST,
        )



@api_view(["GET", "PUT", "DELETE"])
def ropa_detail(request, pk):
    ropa = get_object_or_404(Ropa, pk=pk)
    
    # Traer una sola ropa 
    if request.method == "GET":
        serializer = RopaSerializer(ropa)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Modificar una ropa
    if request.method == "PUT":
        serializer = RopaSerializer(ropa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"mensaje": "Ropa Actualizada"}, status=status.HTTP_200_OK
            )
        return Response(
            {"mensaje": "No se Actualizó porque no es válido"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Borrar ropa
    if request.method == "DELETE":
        ropa.delete()
        return Response(
            {"mensaje": "Ropa Borrada"},
            status=status.HTTP_200_OK,
        )


@api_view(['GET','POST'])
def proveedores_list(request):
    # Traer todos los proveedores
    if request.method == 'GET':
        proveedores = Proveedor.objects.all().select_related()
        serializer = ProveedorSerializer(proveedores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Agregar un proveedor
    if request.method == "POST":
        serializer = ProveedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"mensaje": "Proveedor creado"}, status=status.HTTP_201_CREATED
            )
        return Response(
            {"mensaje": "No se creó porque no es válido"},
            status=status.HTTP_400_BAD_REQUEST,
        )

@api_view(["GET","PUT","DELETE"])
def proveedor_detail(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)

    # Traer un proveedor
    if request.method == "GET":
        serializer = ProveedorSerializer(proveedor)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Modificar un proveedor
    if request.method == "PUT":
        serializer = ProveedorSerializer(proveedor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"mensaje": "Proveedor Actualizado"}, status=status.HTTP_200_OK
            )
        return Response(
            {"mensaje": "No se Actualizó porque no es válido"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Borrar proveedor
    if request.method == "DELETE":
        proveedor.delete()
        return Response(
            {"mensaje": "Proveedor Borrado"},
            status=status.HTTP_200_OK,
        )

    