from django.shortcuts import render
from .models import Aluno

def listar_alunos(request):
    alunos = Aluno.objects.all()

    return render(request, "aluno/lista.html", {
        "alunos": alunos
    })