from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.messages import constants

def autenticar(request):
    if request.method == "GET":
        return render(request, 'autenticar.html')

    elif request.method == "POST": 
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        confirmar_senha = request.POST.get('confirm-password')
        
        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem')
            return redirect('/auth/autenticar')

        if len(username.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 :
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/auth/autenticar')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usário com esse nome')
            return redirect('/auth/autenticar')
        
        try:
            user = User.objects.create_user(
                username=username, password=senha, email=email)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Usuário criado com sucesso')

            return redirect('/auth/logar')

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/auth/autenticar')
 

def logar(request):
    if request.method == 'GET':
        return render(request, 'logar.html')
        
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('password')

        username = auth.authenticate(username=username, password=senha)

        if not username:
            messages.add_message(request, constants.ERROR, 'Nome ou senha inválidos')
            return redirect('/auth/logar')
        else:
            auth.login(request, username)
            return redirect('/cadastro/index.html')


def sair(request):
    auth.logout(request)
    return redirect('/auth/logar')
