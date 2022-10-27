from django.shortcuts import render
from .forms import ContactoForm

#from .models import Producto

# Create your views here.
def index(request):
    mensaje = None
    if(request.method == 'POST'):
        contacto_form = ContactoForm(request.POST)
        if (contacto_form.is_valid()):
            #debería agregar las acciones que necesito hacer
            #contacto_form.save() #para guardar el formulario en el admin
            mensaje= 'Datos recibidos, muchas gracias por contactarnos!'
        else:
            mensaje= 'Error al completar el formulario!'
    else:
        contacto_form = ContactoForm()

    '''
    productos = Producto.object.all()
    data = {
        'productos': productos
    }
    return render(request,'e_commerce/publica/index.html',data
                    {'contacto_form':contacto_form,
                    'mensaje':mensaje})
    '''
    return render(request,'e_commerce/publica/index.html',
                    {'contacto_form':contacto_form,
                    'mensaje':mensaje})
