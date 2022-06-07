from django.urls import path
from .import views

urlpatterns = [
    path('aluno/', views.aluno, name="aluno"),
    path('escola/', views.escola, name="escola"),
    path('responsavel/', views.responsavel, name="responsavel"),
    path('transportador/', views.transportador, name="transportador"),
    path('cad_usuario/', views.cad_usuario, name="cad_usuario"),

]