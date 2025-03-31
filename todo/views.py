from django.shortcuts import render
from .models import Tarea

def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'todo/home.html', {'tareas': tareas})

def agregar(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save()
            return redirect('home.html')
    else:
        form = TareaForm()
        context = {'form': form}
    return render(request, 'todo/agregar.html', context)

def eliminar_tarea(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.delete()
    return redirect('home.html')

def home(request):
    tareas = Tarea.objects.all()
    return render(request, 'todo/home.html', {'tareas': tareas})