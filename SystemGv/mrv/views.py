# views.py

from django.shortcuts import render, redirect
from .forms import ReceituarioForm
from .models import Receituario

def criar_receituario(request):
    if request.method == 'POST':
        form = ReceituarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_receituarios')  # Certifique-se de que está correto
    else:
        form = ReceituarioForm()

    return render(request, 'criar_receituario.html', {'form': form})

def lista_receituarios(request):
    receituarios = Receituario.objects.all()
    return render(request, 'lista_receituarios.html', {'receituarios': receituarios})