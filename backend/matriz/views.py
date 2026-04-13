from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Plato, Venta
from django.db.models import Sum
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import JsonResponse
from .models import Plato # Asegúrate de que el import sea correcto según tu carpeta

def api_detalle_plato(request, plato_id): 
    # ... resto del código igual ...
    try:
        # Buscamos el plato por su campo ID (que definiste como AutoField)
        plato = Plato.objects.get(ID=plato_id)
        
        # Estructuramos el JSON
        data = {
            "id_interno": plato.ID,
            "nombre_producto": plato.nombre,
            "precio": float(plato.precio_venta), # Convertimos Decimal a float para JSON
            "categoria_actual": plato.categoria,
            "status_qa": "Data Verified"
        }
        return JsonResponse(data, safe=False)
        
    except Plato.DoesNotExist:
        # Si el ID no existe, devolvemos un 404 controlado en JSON
        # Esto evita que el socket se cuelgue
        return JsonResponse({"error": "Plato no encontrado en la base de datos"}, status=404)
        
    except Exception as e:
        # Cualquier otro error (de servidor) se reporta limpiamente
        return JsonResponse({"error": str(e)}, status=500)

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

@login_required 
def dashboard_bcg(request):
    platos = Plato.objects.all()
    lista_analisis = []
    total_ventas_acumuladas = 0
    total_margen_acumulado = 0

    for plato in platos:
        ventas_qty = plato.total_ventas()
        margen_unitario = float(plato.margen_contribucion())
        lista_analisis.append({
            'nombre': plato.nombre,
            'objeto': plato,
            'ventas': ventas_qty,
            'margen': margen_unitario,
        })
        total_ventas_acumuladas += ventas_qty
        total_margen_acumulado += margen_unitario

    num_platos = platos.count() or 1
    promedio_ventas = total_ventas_acumuladas / num_platos
    promedio_margen = total_margen_acumulado / num_platos

    for item in lista_analisis:
        if item['ventas'] >= promedio_ventas and item['margen'] >= promedio_margen:
            item['categoria_bcg'] = 'ESTRELLA'
            item['clase_bootstrap'] = 'bg-success'
            item['color_grafico'] = '#198754'
        elif item['ventas'] >= promedio_ventas and item['margen'] < promedio_margen:
            item['categoria_bcg'] = 'VACA'
            item['clase_bootstrap'] = 'bg-warning text-dark'
            item['color_grafico'] = '#ffc107'
        elif item['ventas'] < promedio_ventas and item['margen'] >= promedio_margen:
            item['categoria_bcg'] = 'INTERROGANTE'
            item['clase_bootstrap'] = 'bg-info text-white'
            item['color_grafico'] = '#0dcaf0'
        else:
            item['categoria_bcg'] = 'PERRO'
            item['clase_bootstrap'] = 'bg-danger'
            item['color_grafico'] = '#dc3545'
    contexto = {
        'platos': lista_analisis,
        'p_ventas': promedio_ventas,
        'p_margen': promedio_margen,
        'nombres_js': [item['nombre'] for item in lista_analisis],
        'ventas_js': [item['ventas'] for item in lista_analisis],
        'margenes_js': [item['margen'] for item in lista_analisis],
    }

    return render(request, 'dashboard.html', contexto)