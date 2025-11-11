def menu_roles(request):
    menu = []

    if request.user.is_authenticated:
        roles = request.user.groups.values_list('name', flat=True)

        # Pacientes
        if 'Admin' in roles or 'Medico' in roles:
            menu.append({'name': 'Pacientes', 'url_name': 'citas:paciente-list'})

        # Especialidades
        if 'Admin' in roles or 'Medico' in roles:
            menu.append({'name': 'Especialidades', 'url_name': 'citas:especialidad-list'})

        # Médicos
        if 'Admin' in roles:
            menu.append({'name': 'Médicos', 'url_name': 'citas:medico-list'})

        # Citas
        if set(roles) & {'Admin', 'Medico', 'Paciente'}:
            menu.append({'name': 'Citas', 'url_name': 'citas:cita-list'})

    return {'menu_roles': menu}
