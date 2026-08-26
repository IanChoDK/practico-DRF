from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Ropa
from .serializers import RopaSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def ropa_list(request):
    if request.method == 'GET':
        ropa = Ropa.objects.all()
        serializer = RopaSerializer(ropa, many=True)
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