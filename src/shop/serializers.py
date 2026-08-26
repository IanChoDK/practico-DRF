from rest_framework import serializers

from .models import Ropa


class RopaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ropa
        fields = [
            "id",
            "nombre",
            "descripcion",
            "precio",
            "categoria",
            "fecha_creacion",
            "fecha_modificacion",
        ]
        read_only_fields= ["id", "fecha_creacion", "fecha_modificacion"] 