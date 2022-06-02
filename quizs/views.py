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

def resultados(request,id):
    questions_multiselect = Multiple.objects.filter(quiz_id=id)
    questions_true_false =  True_False.objects.filter(quiz_id=id)
    listCorrectDB = []
    for i in questions_multiselect:
        listCorrectDB.append(str(i.correct))
    for i in questions_true_false:
        listCorrectDB.append(str(i.correct))
    total = len(listCorrectDB)
    puntaje = 0
    resul = request.POST
    for i in listCorrectDB:
        if i in resul.values():
            puntaje += 1

    # respuesta = "Tu puntaje es: %d / %d"%(puntaje,total)
    print(f"Puntaje: {puntaje} de {total}")
    print("---------------------------------------------")
    return render(request, 'resultado.html', {
        "puntaje":puntaje,
        "total":total,
        "n":id
    })
