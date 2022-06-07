import email
from django.forms import EmailField
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import auth, messages
from django.contrib.messages import constants
#from .models import cadastro

# Create your views here.
def aluno(request):
    if request.method == "GET":
        return render(request, 'aluno.html')
    elif request.method == "POST": 
        nome_aluno = request.POST.get('nome_aluno')
        cpf_aluno = request.POST.get('cpf_aluno')
        escola_aluno = request.POST.get('escola_aluno')
        end_escola_aluno = request.POST.get('end_escola_aluno')
       
        #if len(nome_aluno.strip()) == 0 or len(cpf_aluno.strip()) == 0 or len (escola_aluno()) == 0 or len(end_escola_aluno) == 0:
         #   messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
          #  return redirect('/cadastro/aluno')

        #user = User.objects.filter(cpf_aluno = cpf_aluno)

       # if user.exists():
        #    messages.add_message(request, constants.ERROR, 'Já existe um usário com esse CPF')
        #    return redirect('/cadastro/aluno')
        
        try:
            user = User.objects.create_user(nome_aluno=nome_aluno, cpf_aluno=cpf_aluno, escola_aluno=escola_aluno, end_escola_aluno=end_escola_aluno)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Aluno adicionado com sucesso!')

            return redirect('/cadastro/aluno')

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/cadastro/aluno')

        return HttpResponse(Recebido)


def escola(request):
    if request.method == "GET":
        return render(request, 'escola.html')
    elif request.method == "POST": 
        nome_escola = request.POST.get('nome_escola')
        cnpj_escola = request.POST.get('cnpj_escola')
        end_escola = request.POST.get('end_escola')
        tel_escola = request.POST.get('tel_escola')
        email_escola = request.POST.get('email_escola')
        resp_escola = request.POST.get('resp_escola')
       
        if len(nome_escola.strip()) == 0 or len(cnpj_escola.strip()) == 0 or len(end_escola.strip()) == 0 or len(tel_escola.strip()) == 0 or len(email_escola.strip()) == 0 or len(resp_escola.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/cadastro/escola')

        user = User.objects.filter(cnpj_escola = cnpj_escola)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usário com esse CNPJ')
            return redirect('/cadastro/escola')
        
        try:
            user = User.objects.create_user(nome_escola=nome_escola, cnpj_escola=cnpj_escola, end_escola=end_escola, tel_escola=tel_escola, email_escola=email_escola, resp_escola=resp_escola)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Responsável adicionado com sucesso!')

            return redirect('/cadastro/escola')

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/cadastro/escola')

        return HttpResponse(Recebido) 


def responsavel(request):
    if request.method == "GET":
        return render(request, 'responsavel.html')
    elif request.method == "POST": 
        nome_resp = request.POST.get('nome_resp')
        cpf_resp = request.POST.get('cpf_resp')
        email_resp = request.POST.get('email_resp')
        end_resp = request.POST.get('end_resp')
        tel_resp = request.POST.get('tel_resp')
       
        if len(nome_resp.strip()) == 0 or len(cpf_resp.strip()) == 0 or len(email.resp.strip()) == 0 or len(end_resp.strip()) == 0 or len(tel_resp.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/cadastro/responsavel')

        user = User.objects.filter(cpf_resp = cpf_resp)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usário com esse CPF')
            return redirect('/cadastro/responsavel')
        
        try:
            user = User.objects.create_user(nome_resp=nome_resp, cpf_resp=cpf_resp, email_resp=email_resp, end_resp=end_resp, tel_resp=tel_resp)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Responsável adicionado com sucesso!')

            return redirect('/cadastro/aluno')

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/cadastro/responsavel')

        return HttpResponse(Recebido)    


def transportador(request):
    if request.method == "GET":
        return render(request, 'transportador.html')
    elif request.method == "POST": 
        nome_transp = request.POST.get('nome_transp')
        cpf_transp = request.POST.get('cpf_transp')
        email_transp = request.POST.get('email_transp')
        end_transp = request.POST.get('end_transp')
        tel_transp = request.POST.get('tel_transp')
        veiculo = request.POST.get('veiculo')
        placa = request.POST.get('placa')
        capacidade = request.POST.get('capacidade')
        tempo_atua = request.POST.get('tempo_atua')
        escola_atende = request.POST.get('escola_atende')
       
        if len(nome_transp.strip()) == 0 or len(cpf_transp.strip()) == 0 or len(email_transp.strip()) == 0 or len(end_transp.strip()) == 0 or len(tel_transp.strip()) == 0 or len(veiculo.strip()) == 0 or len(placa.strip()) == 0 or len(capacidade.strip()) == 0 or len(tempo_atua.strip()) == 0 or len(escola_atende.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/cadastro/transportador')

        user = User.objects.filter(cpf_transp = cpf_transp)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usário com esse CPF')
            return redirect('/cadastro/transportador')
        
        try:
            user = User.objects.create_user(nome_transp=nome_transp, cpf_transp=cpf_transp, email_transp=email_transp, end_transp=end_transp, tel_transp=tel_transp, veiculo=veiculo, placa=placa, capacidade=capacidade, tempo_atua=tempo_atua, escola_atende=escola_atende)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Transportador adicionado com sucesso!')

            return redirect('/cadastro/rota.html')

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/cadastro/transportador.html')

        return HttpResponse(Recebido)

def cad_usuario(request):
    if request.method == "GET":
        return render(request, 'cad_usuario.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        primeiro_nome = request.POST.get('primeiro_nome')
        ultimo_nome = request.POST.get('ultimo_nome')

        usuario = User.objects.filter(username=username).exclude(id=request.user.id)

        if usuario.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse Username')
            return redirect('/cadastro/cad_usuario')

        request.user.username = username
        request.user.email = email
        request.user.first_name = primeiro_nome
        request.user.last_name = ultimo_nome
        request.user.save()
    
        messages.add_message(request, constants.SUCCESS, 'Dados alterado com sucesso')
        return redirect('/cadastro/cad_usuario')           
