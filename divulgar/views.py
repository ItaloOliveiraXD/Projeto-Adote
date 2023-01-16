from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def novo_pet(request):
    if request.method == 'GET':
        return render(request, 'divulgar/novo_pet.html')
