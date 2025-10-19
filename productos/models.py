from django.db import models

# Create your models here.
class producto(models.Model):
    CATEGORIAS = [
        ('ELECTRONICA', 'Electrónica'),
        ('ROPA', 'Ropa'),
        ('ALACENA', 'Alacena'),
        ('REFRIGERADOS', 'Refrigerados'),
        ('HIGIENE, SALUD, Y BELLEZA', 'Higiene, salud, y belleza'),
        ('HOGAR', 'Hogar'),
        ('DEPORTES', 'Deportes'),
        ('OTROS', 'Otros'),
    ]

    PROVEEDORES = [
        (1020, '1020- Carnes Y Productos de Origen Animal'),
        (2030, '2030- Lacteos y Derivados'),
        (3040, '3040- Electronica y Accesorios'),
        (4050, '4050- Ropa y Calzado'),
        (5060, '5060- Articulos de Hogar'),
        (6070, '6070- Articulos de Deporte'),
        (7080, '7080- Suministros de Higiene y Belleza'),
        (8090, '8090- Productos Varios'),
        (0000, 'N/A'),
    ]
    
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    categoria = models.CharField(max_length=100, choices=CATEGORIAS, default='OTROS')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    descripcion = models.TextField()
    id_proveedor = models.IntegerField(choices=PROVEEDORES, default=0000)
    def __str__(self):
        return f'producto: {self.nombre} - {self.categoria} - ${self.precio}'
    