from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages


def cadastro(request):

    if request.user.is_authenticated:
        return redirect('/divulgar/novo_pet')

    if request.method == "GET":
        return render(request, 'usuarios/cadastro.html')

    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 or len(confirmar_senha.strip()) == 0:  # noqa: E501
            messages.warning(request, 'Preencha todos os campos!')
            return render(request, 'usuarios/cadastro.html')

        if senha != confirmar_senha:
            messages.warning(request, 'As senhas devem ser iguais!')
            return render(request, 'usuarios/cadastro.html')

        try:
            user = authenticate(username=nome)
            if user is not None:
                user_cadastrar = User.objects.create_user(
                    username=nome,
                    email=email,
                    password=senha,
                )
                user_cadastrar.full_clean()
                messages.success(request, 'Cadastrado com sucesso!')
                return render(request, 'usuarios/cadastro.html')
            else:
                messages.warning(request, 'Usuário já existe!')
                return render(request, 'usuarios/cadastro.html')

        except (ValueError):
            messages.error(request, 'Error interno do sistema.')
            return render(request, 'usuarios/cadastro.html')


def logar(request):

    if request.user.is_authenticated:
        return redirect('/divulgar/novo_pet')

    if request.method == 'GET':
        return render(request, 'usuarios/login.html')

    elif request.method == "POST":
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        user = authenticate(
            username=nome,
            password=senha,
        )

        if user is not None:
            login(request, user)
            return redirect('/divulgar/novo_pet')
        else:
            messages.warning(request, 'Usuário ou senha incorreto!')
            return render(request, 'usuarios/login.html')


def sair(request):
    logout(request)
    return redirect('/auth/login')
