import email
from django.forms import EmailField
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import auth, messages
from django.contrib.messages import constants

def conta(request):
    if request.method == "GET":
        return render(request, 'conta.html')
    elif request.method == "POST": 
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        confirmar_senha = request.POST.get('confirm-password')
        
        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem')
            return redirect('/auth/conta')

        if len(username.strip()) == 0 or len(senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/auth/conta')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usário com esse nome')
            return redirect('/auth/conta')
        
        try:
            user = User.objects.create_user(username=username, password=senha)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Usuário criado com sucesso')

            return redirect('/auth/logar')

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/auth/conta')

        return HttpResponse(Recebido)    




def logar(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('https:/uniescolar.herokuapp.com')
        return render(request, 'logar.html')
        
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('password')

        usuario = auth.authenticate(username=username, password=senha)

        if not usuario:
            messages.add_message(request, constants.ERROR, 'Nome ou senha inválidos')
            return redirect('/auth/logar')
        else:
            auth.login(request, usuario)
            return redirect('/plataforma')


def sair(request):
    auth.logout(request)
    return redirect('/auth/logar')
