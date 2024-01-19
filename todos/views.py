from django.shortcuts import render
from django.http import HttpResponse # deve puxar o http response
# Create your views here.

def home(request):
    return render(request, "todos/home.html") #colocar o render para usar o html 

#deve ser criada uma pasta com o nome template depois o nome do projeto e o html