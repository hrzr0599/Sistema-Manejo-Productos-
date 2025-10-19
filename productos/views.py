from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import producto
from .forms import ProductoForm

# Create your views here.
def index(request):
    return render(request, 'productos/index.html', {
        'productos': producto.objects.all()
        })

def ver_producto(request, id):
    product = producto.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def agregar(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            nuevo_nombre=form.cleaned_data['nombre']
            nuevo_categoria=form.cleaned_data['categoria']
            nuevo_precio=form.cleaned_data['precio']
            nuevo_stock=form.cleaned_data['stock']
            nuevo_descripcion=form.cleaned_data['descripcion']
            nuevo_id_proveedor=form.cleaned_data['id_proveedor']

            nuevo_producto = producto(
                nombre=nuevo_nombre,
                categoria=nuevo_categoria,
                precio=nuevo_precio,
                stock=nuevo_stock,
                descripcion=nuevo_descripcion,
                id_proveedor=nuevo_id_proveedor
            )
            nuevo_producto.save()
            return render(request, 'productos/agregar.html', {
                'form': ProductoForm(),
                'success': True
            })
    else:
        form = ProductoForm()
    return render(request, 'productos/agregar.html', {
        'form': ProductoForm()
    })

def editar(request, id):
    if request.method == 'POST':
        product = producto.objects.get(pk=id)
        form = ProductoForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return render(request, 'productos/editar.html', {
                'form': form,
                'success': True
            })
    else:
        product = producto.objects.get(pk=id)
        form = ProductoForm(instance=product)
    return render(request, 'productos/editar.html', {
        'form': form,
        'success': False
    })

def eliminar(request, id):
  if request.method == 'POST':
    product = producto.objects.get(pk=id)
    product.delete()
  return HttpResponseRedirect(reverse('index'))