from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages


def cadastro(request):

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
            user = User.objects.create_user(
                username=nome,
                email=email,
                password=senha,
            )
            user.full_clean()
            messages.success(request, 'Cadastrado com sucesso!')
            return render(request, 'usuarios/cadastro.html')
        except (ValueError):
            messages.error(request, 'Error interno do sistema.')
            return render(request, 'usuarios/cadastro.html')
