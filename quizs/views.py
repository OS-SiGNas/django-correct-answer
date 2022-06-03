from django.shortcuts import render
from .models import Quiz, Multiple, True_False


def menu_quizs(request):
    return render(request, 'menu_quizs.html',{'quizs':Quiz.objects.all()})

def render_quizs(request,id):
    return render(request, 'quizs_template.html',{
        "quiz":Quiz.objects.get(id=id),
        "questionsMultiselect":Multiple.objects.filter(quiz_id=id),
        "questionsTrueFalse":True_False.objects.filter(quiz_id=id)
    })

def results(request,id):
    # creando lista respuestas correctas traidas de la base de datos
    questions_multiselect = Multiple.objects.filter(quiz_id=id)
    questions_true_false =  True_False.objects.filter(quiz_id=id)
    listCorrectDB=[]
    for i in questions_multiselect:
        listCorrectDB.append(str(i.correct))
    for i in questions_true_false:
        listCorrectDB.append(str(i.correct))
    print("s --->", listCorrectDB)

    # Creando lista de respuestas recibidas por http
    resul_list = list(request.POST.values())
    resul_list.pop(0)
    print("r --->", resul_list)

    total = len(listCorrectDB) # Cantidad de preguntas en el Quiz 
    scores = 0

    # Comparando Respuestas correctas en ambas listas
    for i in range(total):
        if listCorrectDB[i] == resul_list[i]:
            scores += 1

    print(f" ====== Puntaje: {scores} de {total} ====== ")

    return render(request, 'resultado.html', {
        "scores":scores,
        "total":total,
        "n":id
    })
