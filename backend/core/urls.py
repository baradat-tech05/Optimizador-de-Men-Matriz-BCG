from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.views.generic import RedirectView
from django.urls import reverse_lazy
from matriz.views import dashboard_bcg, api_detalle_plato

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Autenticación
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Registro
    path('signup/', CreateView.as_view(
        template_name='registration/signup.html',
        form_class=UserCreationForm,
        success_url=reverse_lazy('login')
    ), name='signup'),

    # RUTA PARA EL GRÁFICO (Asegúrate de que sea dashboard/ con la barra al final)
    path('dashboard/', dashboard_bcg, name='dashboard'),
    
    # Redirigir la raíz al login
    path('', RedirectView.as_view(url='/accounts/login/', permanent=False)),

    # API endpoint para detalles del plato
    path('api/platos/<int:plato_id>/', api_detalle_plato, name='api_detalle_plato'),
]
