from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Color(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Talle(models.Model):
    nombre_talle = models.CharField(max_length=5)

    def __str__(self):
        return self.nombre_talle

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Ropa(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,related_name="productos")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    talle = models.ForeignKey(Talle, on_delete= models.CASCADE, related_name="productos")
    color = models.ForeignKey(Color, on_delete= models.CASCADE, related_name="productos")
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name="productos")

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"