from django import forms
# importar los modelos
from .models import Paciente, Medico, Cita, Especialidad


# crear formulario para Especialidad
class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        # campos del formulario
        fields = ['nombre_especialidad', 'descripcion']
        widgets = {
            'nombre_especialidad': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


# crear formulario para Paciente
class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        # campos del formulario
        fields = ['nombre', 'apellido', 'telefono', 'correo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
        }


# crear formulario para Medico
class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        # campos del formulario
        fields = ['nombre', 'apellido', 'telefono', 'correo', 'especialidad']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'especialidad': forms.Select(attrs={'class': 'form-control'}),
        }


# crear formulario para Cita
class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        # campos del formulario
        fields = ['medico', 'paciente', 'fecha_hora', 'motivo', 'estado']
        widgets = {
            'medico': forms.Select(attrs={'class': 'form-control'}),
            'paciente': forms.Select(attrs={'class': 'form-control'}),
            'fecha_hora': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'motivo': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }
