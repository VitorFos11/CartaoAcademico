from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Aluno


def listar_alunos(request):

    alunos = Aluno.objects.all()

    return render(request, "aluno/lista.html", {
        "alunos": alunos
    })



def criar_aluno(request):

    if request.method == "POST":

        nome = request.POST["nome"]
        curso = request.POST["curso"]
        bio = request.POST.get("bio", "")

        Aluno.objects.create(
            nome=nome,
            curso=curso,
            bio=bio
        )

        messages.success(
        request,
        "Aluno cadastrado com sucesso!"
        )   

        
        return redirect("listar_alunos")


    return render(request, "aluno/form_aluno.html", {
        "titulo": "Novo Aluno"
    })




def editar_aluno(request, pk):

    aluno = get_object_or_404(Aluno, pk=pk)


    if request.method == "POST":

        aluno.nome = request.POST["nome"]

        aluno.curso = request.POST["curso"]

        aluno.bio = request.POST.get("bio", "")

        aluno.save()

        messages.success(
        request,
        "Aluno atualizado com sucesso!"
        )   

        return redirect("listar_alunos")


    return render(request, "aluno/form_aluno.html", {

        "aluno": aluno,

        "titulo": f"Editar: {aluno.nome}"

    })






def excluir_aluno(request, pk):

    aluno = get_object_or_404(Aluno, pk=pk)


    if request.method == "POST":

        aluno.delete()

        messages.success(
        request,
        "Aluno excluído com sucesso!"
        )
        
        return redirect("listar_alunos")


    return render(request, "aluno/confirmar_exclusao.html", {

        "aluno": aluno

    })