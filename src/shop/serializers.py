from rest_framework import serializers

from .models import Ropa, Categoria, Color, Proveedor, Talle

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"
        read_only_fields = ["id"]


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"
        read_only_fields = ["id"]


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ["nombre","telefono","activo"]
        read_only_fields = ["id"]


class TalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talle
        fields = ["nombre_talle"]
        read_only_fields = ["id"]


class RopaPublicSerializer(serializers.ModelSerializer):
    # Serializers anidados
    categoria = CategoriaSerializer(read_only=True)
    talle = TalleSerializer(read_only=True)
    
    class Meta:
        model = Ropa
        fields = [
            "id",
            "nombre",
            "descripcion",
            "precio",
            "categoria",
            "talle"
        ]
        read_only_fields = ["id", "fecha_creacion", "fecha_modificacion"]


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
            "color",
            "proveedor",
            "talle"
        ]
        read_only_fields= ["id", "fecha_creacion", "fecha_modificacion"] 

