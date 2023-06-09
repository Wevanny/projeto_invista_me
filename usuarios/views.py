from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm


# Create your views here.
def novo_usuario(request):
    # verificar tipo, validar requisição, informar criação do usuário, salvar no banco de dados
    if request.method == 'POST':        
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            # informar o usuário
            usuario = formulario.cleaned_data.get('username')
            messages.success(request, f'O usuário {usuario} foi criado com sucesso!')
            return redirect('login')
            # salvar no banco de dados
    else:
        formulario = UserRegisterForm()

    return render(request, 'usuarios/registrar.html', {'formulario': formulario})
