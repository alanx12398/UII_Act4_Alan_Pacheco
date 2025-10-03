from django.shortcuts import render

# Create your views here.
def index(request):
    alumnos = [
        {'nombre': 'Juan', 'edad': 20, 'carrera': 'Ingeniería Informática'},
        {'nombre': 'María', 'edad': 22, 'carrera': 'Diseño Gráfico'},
        {'nombre': 'Pedro', 'edad': 21, 'carrera': 'Administración de Empresas'},
    ]
    return render(request, 'index.html', {'alumnos': alumnos})
