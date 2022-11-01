from django.db import models

# Create your models here.

class Categoria(models.Model):
    #id = models.AutoField(primary_key=True)->no es necesario tenerlo
    nombre = models.CharField(max_length=50, editable=False) #para que no se pueda editar

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    #id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT) #verbose_name para modificar el nombre
    descripcion = models.TextField(blank=True) #equivalente a null=True para que no se tenga que completar el campo
    #nuevo = models.BooleanField(default=True)
    #fecha_fabricacion = models.DateTimeField()
    imagen = models.ImageField(upload_to="producto", null=True)

    def __str__(self):
        return self.nombre

class Persona(models.Model):
    #id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    #estado = models.BooleanField()
    #edad = models.IntegerField()
    #imagen = models.ImageField() #para usar imágenes, hay que hacer: pip install Pillow
    #data = models.DateField()
    #urls = models.URLField()
    #archivo = models.FileField()

    def __str__(self):
        return self.nombre #str(self.id)

#para crear las tablas en sqlite:
#python manage.py makemigrations
#python manage.py migrate

#para crear las tablas en pgadmin:
#agregar la contraseña en database del archivo settings.py
#python manage.py makemigrations
#python manage.py migrate

#para crear un usuario en el admin de django:
#python manage.py createsuperuser: admin, tuslibros123




