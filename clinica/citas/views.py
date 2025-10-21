from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .models import Paciente, Medico, Cita, Especialidad
# importar reverse_lazy para redirecciones
from django.urls import reverse_lazy
# importar formularios personalizados
from .forms import PacienteForm, MedicoForm, CitaForm, EspecialidadForm

# Create your views here.


# vista generica para Especialidades
class EspecialidadListView(ListView):
    model = Especialidad
    fields = ['nombre_especialidad', 'descripcion']
    template_name = "especialidades/especialidad-list.html"
    context_object_name = "especialidades"
    

# vista generica para agregar Especialidades
class EspecialidadCreateView(CreateView):
    model = Especialidad
    form_class = EspecialidadForm
    template_name = "especialidades/especialidad-form.html"
    success_url = reverse_lazy("citas:especialidad-list")


# vista generica para Pacientes
class PacienteListView(ListView):
    model = Paciente
    fields = ['nombre', 'apellido', 'telefono', 'correo']
    template_name = "pacientes/paciente-list.html"
    context_object_name = "pacientes"


# vista generica para agregar Pacientes
class PacienteCreateView(CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = "pacientes/paciente-form.html"
    success_url = reverse_lazy("citas:paciente-list")


# vista generica para Medicos
class MedicoListView(ListView):
    model = Medico
    fields = ['nombre', 'apellido', 'telefono', 'correo', 'especialidad']
    template_name = "medicos/medico-list.html"
    context_object_name = "medicos"


# vista generica para agregar Medicos
class MedicoCreateView(CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = "medicos/medico-form.html"
    success_url = reverse_lazy("citas:medico-list")


# vista generica para Citas
class CitaListView(ListView):
    model = Cita
    fields = ['medico', 'paciente', 'fecha_hora', 'motivo', 'estado']
    template_name = "citas/cita-list.html"
    context_object_name = "citas"


# vista generica para agregar Citas
class CitaCreateView(CreateView):
    model = Cita
    form_class = CitaForm
    template_name = "citas/cita-form.html"
    success_url = reverse_lazy("citas:cita-list")
    
    
# vista generica para actualizar Citas
class CitaUpdateView(UpdateView):
    model = Cita
    form_class = CitaForm
    template_name = "citas/cita-update.html"
    success_url = reverse_lazy("citas:cita-list")
