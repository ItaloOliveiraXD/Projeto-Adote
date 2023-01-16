from django.shortcuts import render


def novo_pet(request):
    if request.method == 'GET':
        return render(request, 'divulgar/novo_pet.html')
