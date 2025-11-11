from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView
from .models import Paciente, Medico, Cita, Especialidad
# importar reverse_lazy para redirecciones
from django.urls import reverse_lazy
# importar formularios personalizados
from .forms import PacienteForm, MedicoForm, CitaForm, EspecialidadForm

# Create your views here.


class RoleRequiredMixin(UserPassesTestMixin):
    allowed_roles = []
    
    def test_func(self):
        user = self.request.user
        if user.is_superuser:
            return True
        return user.groups.filter(name__in=self.allowed_roles).exists()

    def handle_no_permission(self):
        from django.shortcuts import redirect
        return redirect('login')


# vista generica para Especialidades
class EspecialidadListView(LoginRequiredMixin, RoleRequiredMixin, ListView):
    model = Especialidad
    fields = ['nombre_especialidad', 'descripcion']
    template_name = "especialidades/especialidad-list.html"
    context_object_name = "especialidades"
    allowed_roles = ['Admin']
    

# vista generica para agregar Especialidades
class EspecialidadCreateView(LoginRequiredMixin, RoleRequiredMixin, CreateView):
    model = Especialidad
    form_class = EspecialidadForm
    template_name = "especialidades/especialidad-form.html"
    success_url = reverse_lazy("citas:especialidad-list")
    allowed_roles = ['Admin']


# vista generica para Pacientes
class PacienteListView(LoginRequiredMixin, RoleRequiredMixin, ListView):
    model = Paciente
    fields = ['nombre', 'apellido', 'telefono', 'correo']
    template_name = "pacientes/paciente-list.html"
    context_object_name = "pacientes"
    allowed_roles = ['Admin']


# vista generica para agregar Pacientes
class PacienteCreateView(LoginRequiredMixin, RoleRequiredMixin, CreateView):
    model = Paciente
    form_class = PacienteForm
    template_name = "pacientes/paciente-form.html"
    success_url = reverse_lazy("citas:paciente-list")
    allowed_roles = ['Admin']


# vista generica para Medicos
class MedicoListView(LoginRequiredMixin, RoleRequiredMixin, ListView):
    model = Medico
    fields = ['nombre', 'apellido', 'telefono', 'correo', 'especialidad']
    template_name = "medicos/medico-list.html"
    context_object_name = "medicos"
    allowed_roles = ['Admin']


# vista generica para agregar Medicos
class MedicoCreateView(LoginRequiredMixin, RoleRequiredMixin, CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = "medicos/medico-form.html"
    success_url = reverse_lazy("citas:medico-list")
    allowed_roles = ['Admin']


# vista generica para Citas
class CitaListView(LoginRequiredMixin, RoleRequiredMixin, ListView):
    model = Cita
    fields = ['medico', 'paciente', 'fecha_hora', 'motivo', 'estado']
    template_name = "citas/cita-list.html"
    context_object_name = "citas"
    allowed_roles = ['Admin', 'Medico', 'Paciente']


# vista generica para agregar Citas
class CitaCreateView(LoginRequiredMixin, RoleRequiredMixin, CreateView):
    model = Cita
    form_class = CitaForm
    template_name = "citas/cita-form.html"
    success_url = reverse_lazy("citas:cita-list")
    allowed_roles = ['Admin']
    
    
# vista generica para actualizar Citas
class CitaUpdateView(LoginRequiredMixin, RoleRequiredMixin, UpdateView):
    model = Cita
    form_class = CitaForm
    template_name = "citas/cita-update.html"
    success_url = reverse_lazy("citas:cita-list")
    allowed_roles = ['Admin', 'Medico']
