from django.db import models

# Create your models here.
'''
class Marca(models.Model):
    nombre = models.Charfield(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model()):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    nuevo = models.BooleanField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    fecha_fabricacion = models.DateField()
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre

# sqlite
#ejecutar python manage.py makemigrations
#ejecutar python manage.py migrate

'''



