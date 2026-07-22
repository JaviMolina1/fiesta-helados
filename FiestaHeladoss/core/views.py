
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .models import Barquillo, Helados, Boleta, detalle_boleta
from .forms import HeladoForm, RegistroUserForm
from core.compras import Carrito
from .forms import HeladoForm, RegistroUserForm, User, PerfilModificacion
from django.contrib import messages




# Create your views here.
def Home(request):
    return render(request, 'Home.html')

def Disponibilidad(request):
    return render(request, 'Disponibilidad.html')

def perfil(request):
    return render(request, 'perfil.html')

def Servicio(request):
    return  render(request, 'Servicio.html')

def Sugerencias(request):
    return render(request, 'Sugerencias.html')

def Valores(request):
    return render(request, 'Valores.html')

def Aspectos(request):
    return render(request, 'Aspectos.html')


@login_required
def Productos(request):
    datos = Helados.objects.all()          #similar select * from Vehiculo
    return render(request, 'Productos.html', {"datos":datos})

def crear(request): 
    if request.method=='POST':
        heladoform = HeladoForm(request.POST, request.FILES)
        if heladoform.is_valid():
            heladoform.save()         #similar a insert into
            return redirect ('Productos')
    else:
        heladoform=HeladoForm()
    return render (request, 'crear.html',{'heladoform':heladoform})

def detalle(request, id):
    helado = get_object_or_404(Helados, id=id)
    return render(request, 'detalle.html', {'helado':helado})    

def modificar(request, id):
    helado = Helados.objects.get(id=id)      #devuelve un objeto
    datos={
        'formModificar': HeladoForm(instance=helado),    #devuelve un objeto de tipo form
        'helado': helado
    }
    if request.method=='POST':
        formulario = HeladoForm(request.POST, request.FILES, instance=helado)   #instanciamos un obj para almacenarlo en el backend
        if formulario.is_valid():
            formulario.save()           #actualiza la instancia de objeto vehiculo
            return redirect ('Productos')
    return render(request, 'modificar.html', datos)

def eliminar(request, id):
    helado = get_object_or_404(Helados, id=id)
    if request.method=='POST':
        if 'elimina' in request.POST:           #si el botón elimina es seleccionado
            helado.delete()                   #elimina el objeto del backend
            return redirect('Productos')
    return render(request, 'eliminar.html',{'helado': helado})

def cerrar(request):
    logout(request)
    return redirect('Home')


def registrar(request):
    data={                          #parámetro que llega al template
        'form': RegistroUserForm()
    }
    if request.method=="POST":
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()       #crear un objeto en el backend
            user = authenticate(username=formulario.cleaned_data["username"], 
                    password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect('Home') 
        data["form"]=formulario           
    return render(request, 'registration/registrar.html',data)



def agregar_producto(request,id):
    carrito_compra= Carrito(request)
    helado = Helados.objects.get(id=id)
    carrito_compra.agregar(helado=helado)
    return redirect('tienda')

def eliminar_producto(request, id):
    carrito_compra= Carrito(request)
    helado = Helados.objects.get(id=id)
    carrito_compra.eliminar(helado=helado)
    return redirect('tienda')

def restar_producto(request, id):
    carrito_compra= Carrito(request)
    helado = Helados.objects.get(id=id)
    carrito_compra.restar(helado=helado)
    return redirect('tienda')

def limpiar_carrito(request):
    carrito_compra= Carrito(request)
    carrito_compra.limpiar()
    return redirect('tienda')    

def tienda(request):
    helados = Helados.objects.all()
    datos={
        'helados':helados
    }
    return render(request, 'tienda.html', datos)

def generarBoleta(request):
    precio_total=0
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + int(value['precio']) * int(value['cantidad'])
    boleta = Boleta(total = precio_total)
    boleta.save()
    productos = []
    for key, value in request.session['carrito'].items():
            producto = Helados.objects.get(id = value['helado_id'])
            cant = value['cantidad']
            subtotal = cant * int(value['precio'])
            detalle = detalle_boleta(id_boleta = boleta, id_producto = producto, cantidad = cant, subtotal = subtotal)
            detalle.save()
            productos.append(detalle)
    datos={
        'productos':productos,
        'fecha':boleta.fechaCompra,
        'total': boleta.total
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'detallecarrito.html',datos) 

def perfilmod(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = PerfilModificacion(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos modificados')
            return redirect('perfil')
    else:
        form = PerfilModificacion(instance=user)
    return render(request, 'perfilmod.html', {'modificarperfil': form})


    