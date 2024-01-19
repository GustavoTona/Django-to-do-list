#View é uma função de retorno vinculado a um a url no arquivo url 
#Nao exite uma url sem uma funcao no view
#Serve para banco de dados tambem

from django.shortcuts import render
from django.http import HttpResponse #importando a classe http response


def index(request): #funcao index para receber request com o texto alo mundo
    return HttpResponse ("Olá mundo!")

# depois de feita a funcao index, precisamos linkar ela no url como descrito ali em cima