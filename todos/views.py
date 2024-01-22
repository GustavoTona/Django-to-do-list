from django.shortcuts import render
# deve puxar o http response

from .models import Todo  # vamos na pasta models pegar a classe Todo

def todo_list(request):
    todos = Todo.objects.all() #classe de modelo precisa de um objects para pegas no banco de dados

#colocar o render para renderizar o html 
    return render(request, "todos/todo_list.html", {"todos": todos}) #nome pegar do banco de dados e aparecer no html

#deve ser criada uma pasta com o nome template depois o nome do projeto e o html
