from django import forms
from .models import producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = producto
        fields = ['nombre', 'categoria', 'precio', 'stock', 'descripcion', 'id_proveedor']
        labels = {
            'nombre': 'Nombre del Producto',
            'categoria': 'Categoría',
            'precio': 'Precio',
            'stock': 'Cantidad en Stock',
            'descripcion': 'Descripción',
            'id_proveedor': 'ID del Proveedor',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'id_proveedor': forms.Select(attrs={'class': 'form-control'}),
        }