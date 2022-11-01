from django.shortcuts import render, redirect
from .models import *
from .forms import ContactoForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

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

def registro(request):

    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            #form.save()
            username = form.cleaned_data["username"]
            #user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password1"]])
            #login(request, user)
            messages.success(request, f'Usuario {username} creado')
            return redirect(to="index")
    else:
        form = UserRegisterForm()

    data = { 'form': form  }
   
    return render(request, 'registration/registro.html', data)