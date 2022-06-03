from django.contrib import admin
from django.urls import path
from quizs.views import menu_quizs, results, render_quizs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu_quizs),
    path('quiz/<int:id>', render_quizs),
    path('resultados/<int:id>', results)
]
