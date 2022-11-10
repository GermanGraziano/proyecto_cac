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


class Libro(models.Model):
    titulo = models.CharField(max_length = 150, verbose_name = 'Titulo')
    reseña = models.TextField(null = True, verbose_name = 'Reseña')
    autor = models.CharField(max_length = 100)
    stock = models.IntegerField(verbose_name = 'Stock')
    precio = models.FloatField(verbose_name = 'Precio')
    categoria = models.ManyToManyField(Categoria)
    
class Autor(models.Model):
    autor_nombre = models.CharField(max_length = 100)
    autor_apellido = models.CharField(max_length = 100)
    autor_nacionalidad = models.CharField(max_length = 50)
    libro = models.ManyToManyField(Libro)

class Ingreso(models.Model):
    ingreso_cantidad = models.IntegerField(verbose_name = 'Cantidad Ingresada')
    libro = models.ForeignKey(Libro, ondelete = models.CASCADE)

class Cliente(models.Model):
    nombre = models.CharField(max_length = 100, verbose_name = 'Nombre del Cliente')
    apellido = models.CharField(max_length = 100, verbose_name = 'Apellido del Cliente')
    correo = models.EmailField(max_length = 150, verbose_name = 'Email del Cliente')
    

class Direccion(models.Model):
    calle_y_numero = models.TextField(max_length = 250)
    ciudad = models.CharField(max_length = 100, verbose_name = 'Ciudad')
    provincia = models.CharField(max_length = 100, verbose_name = 'Provincia')
    codigo_postal = models.IntegerField(max_length = 4, verbose_name = 'Codigo Postal')
    cliente = models.ForeignKey(Cliente, ondelete = models.CASCADE)

class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, ondelete = models.CASCADE)
    libro = models.ForeignKey(Libro, ondelete = models.CASCADE)


class Pago(models.Model):
    fecha = models.DateField(verbose_name = 'Fecha de compra')
    total = models.FloatField(verbose_name = 'Total de la compra')
    forma_de_pago = models.CharField(max_length = 75, verbose_name = 'Metodo de pago')
    cliente = models.ForeignKey(Cliente, ondelete = models.PROTECT)
    compra = models.ForeignKey(Compra, ondelete = models.PROTECT)
















#para crear las tablas en sqlite:
#python manage.py makemigrations
#python manage.py migrate

#para crear las tablas en pgadmin:
#agregar la contraseña en database del archivo settings.py
#python manage.py makemigrations
#python manage.py migrate

#para crear un usuario en el admin de django:
#python manage.py createsuperuser: admin, tuslibros123




