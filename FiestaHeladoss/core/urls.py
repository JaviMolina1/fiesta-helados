from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('Disponibilidad/', views.Disponibilidad, name="Disponibilidad"),
    path('Productos/', views.Productos, name="Productos"),
    path('Servicio/', views.Servicio, name="Servicio"),
    path('Sugerencias/', views.Sugerencias, name="Sugerencias"),
    path('Valores/', views.Valores, name="Valores"),
    path('Aspectos/', views.Aspectos, name="Aspectos"),
    path('crear/', views.crear, name="crear"),
    path('detalle/<id>/', views.detalle, name="detalle"),
    path('modificar/<id>/', views.modificar, name="modificar"),
    path('eliminarpro/<id>/', views.eliminar, name="eliminarpro"),    
    path('logout/', views.cerrar, name="cerrar"),

    path('tienda/',views.tienda, name="tienda"),
    path('agregar/<id>', views.agregar_producto, name="agregar"),
    path('eliminar/<id>', views.eliminar_producto, name="eliminar"),
    path('restar/<id>', views.restar_producto, name="restar"),
    path('limpiar/', views.limpiar_carrito, name="limpiar"),
    path('generarBoleta/', views.generarBoleta,name="generarBoleta"),
    path('registrar/', views.registrar, name="registrar"),
    path('perfil/', views.perfil, name="perfil"),
    path('perfilmod/<username>/', views.perfilmod, name='perfilmod'),





]