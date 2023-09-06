from django.shortcuts import render, redirect
from django.http import HttpResponse
#obtener la información del modelo es decir, recuperar la información
from .models import Hoja
from .form import HojaForm

# Create your views here.
def inicio(request):
     return render(request,'paginas/inicio.html')

def compra_h(request):
    return render(request,'compras/compra.html')

def create_compra(request):
    return render(request,'compras/create.html')

def hojas(request):
    hojas_sec=Hoja.objects.all()
    return render(request,'hojas/index.html',{'hojas':hojas_sec})

def crear_hoja(request):
    formulario=HojaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('hojas')
    return render(request,'hojas/crear.html',{'formulario':formulario})

def editar_hoja(request,id):
    hoja=Hoja.objects.get(id=id)
    formulario=HojaForm(request.POST or None, request.FILES or None, instance=hoja)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('hojas')
    return render(request,'hojas/editar.html',{'formulario':formulario})

def eliminar_hoja(request, id):
    hoja=Hoja.objects.get(id=id)
    hoja.delete()
    return redirect('hojas')#se le envía int:id