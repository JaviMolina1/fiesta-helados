import datetime
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Helados(models.Model):
    id = models.CharField(max_length=5, primary_key=True, verbose_name="Id")
    rango =  models.CharField(max_length=20, verbose_name = "Rango")
    cantidad = models.CharField(max_length=20, verbose_name = "Cantidad")
    sabor = models.CharField(max_length=35, verbose_name = "Sabor")
    imagen = models.ImageField(upload_to="imagenes",null=True, verbose_name="Imagen")
    barquillo = models.ForeignKey('Barquillo', on_delete=models.CASCADE, verbose_name="Barquillo")
    precio=models.IntegerField(blank=True, null=True, verbose_name="Precio")


    def __str__(self):
        return self.id

class Barquillo(models.Model):
    idBarquillo = models.IntegerField(primary_key=True, verbose_name = "Id Barquillo")
    nombreBarquillo = models.CharField(max_length=20, verbose_name = "Nombre Barquillo")

    def __str__(self):
        return self.nombreBarquillo

class Boleta(models.Model):
    id_boleta=models.AutoField(primary_key=True)
    total=models.BigIntegerField()
    fechaCompra=models.DateTimeField(blank=False, null=False, default = datetime.datetime.now)
  
    def __str__(self):
        return str(self.id_boleta)

class detalle_boleta(models.Model):
    id_boleta = models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('Helados', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()

    def __str__(self):
        return str(self.id_detalle_boleta)

