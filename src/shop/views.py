from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Ropa
from .serializers import RopaSerializer, RopaPublicSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def ropa_list(request):
    if request.method == 'GET':
        ropa = Ropa.objects.all()
        serializer = RopaPublicSerializer(ropa, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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
    
    if request.method == "GET":
        serializer = RopaSerializer(ropa)
        return Response(serializer.data, status=status.HTTP_200_OK)

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

    if request.method == "DELETE":
        ropa.delete()
        return Response(
            {"mensaje": "Ropa Borrada"},
            status=status.HTTP_200_OK,
        )