from django.urls import path
# importando las vistas
from .views import (
    # Vistas de Paciente
    PacienteListView,
    PacienteCreateView,
    # Vistas de Especialidad
    EspecialidadListView,
    EspecialidadCreateView,
    # Vistas de Medico
    MedicoListView,
    MedicoCreateView,
    # Vistas de Cita
    CitaListView,
    CitaCreateView,
    CitaUpdateView,
)

# agregar un identificador de enrutamiento
app_name = "citas"

# enrutamiento
urlpatterns = [
    # pacientes
    path('pacientes/', PacienteListView.as_view(), name="paciente-list"),
    path('pacientes/nuevo', PacienteCreateView.as_view(), name="paciente-create"),
    # especialidades
    path('especialidades/', EspecialidadListView.as_view(),
         name="especialidad-list"),
    path('especialidades/nueva', EspecialidadCreateView.as_view(),
         name="especialidad-create"),
    # medicos
    path('medicos/', MedicoListView.as_view(), name="medico-list"),
    path('medicos/nuevo', MedicoCreateView.as_view(), name="medico-create"),
    # citas
    path('citas/', CitaListView.as_view(), name="cita-list"),
    path('citas/nueva', CitaCreateView.as_view(), name="cita-create"),
    path('citas/<int:pk>/editar', CitaUpdateView.as_view(), name="cita-update"),
]
