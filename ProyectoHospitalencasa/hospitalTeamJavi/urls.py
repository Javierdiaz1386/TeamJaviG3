
from django.contrib import admin
from django.urls import path
from hospitalApp.views import PsaludViews, PacienteViews, FamiliarViews, PacienteDetallesViews, PacienteIndividualDetallesViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('crearPsalud/', PsaludViews.as_view(), name='psalud'),
    path('crearPciente/', PacienteViews.as_view(), name='paciente'),
    path('crearFamiliar/', FamiliarViews.as_view(), name='familiar'),
    path('pacienteDetalles/', PacienteDetallesViews.as_view(), name='detallesviews'),
    path('pacienteDetalles/<int:id>', PacienteIndividualDetallesViews.as_view(), name='detallesindividualviews'),
]
