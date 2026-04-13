from django.db import models
from django.db.models import Sum

# ... (clases Ingrediente, Plato, etc.)

class Ingrediente(models.Model):
    # Definir opciones
    UNIDADES_CHOICES = [
        ('GR', 'Gramos'),
        ('KG', 'Kilogramos'),
        ('ML', 'Mililitros'),
        ('LT', 'Litros'),
        ('UN', 'Unidad/Pieza'),
    ]

    ID = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    
    # Cambiar CharField por 'choices' para opciones predefinidas
    unidad_de_medida = models.CharField(
        max_length=100, 
        choices=UNIDADES_CHOICES, 
        default='GR'
    )
    
    precio_costo_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.nombre} ({self.get_unidad_de_medida_display()})"

class Plato(models.Model):
    ID = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nombre

    # --- LÓGICA DE NEGOCIO ---

    def calcular_costo_total(self):
        # Usamos select_related para traer el precio del ingrediente sin hacer mil consultas
        recetas = self.receta_set.select_related('ingrediente').all()
        total = sum(item.cantidad_necesaria * item.ingrediente.precio_costo_unitario for item in recetas)
        return total

    def margen_contribucion(self):
        """Ganancia neta por plato: Precio - Costo"""
        return self.precio_venta - self.calcular_costo_total()

    def total_ventas(self):
        """Suma histórica de unidades vendidas"""
        return Venta.objects.filter(plato=self).aggregate(Sum('cantidad_vendida'))['cantidad_vendida__sum'] or 0

class Receta(models.Model):
    ID = models.AutoField(primary_key=True)
    # La línea que une Recetas con Platos
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    # La línea que une Recetas con Ingredientes
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    cantidad_necesaria = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.plato.nombre} necesita {self.ingrediente.nombre}"

class Venta(models.Model):
    ID = models.AutoField(primary_key=True)
    # La línea que une Ventas con Platos
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    cantidad_vendida = models.IntegerField()
    fecha_venta = models.DateField()

    def __str__(self):
        return f"Venta de {self.plato.nombre} el {self.fecha_venta}"