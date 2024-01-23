

from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View #importando uma lista generica / listview

from django.urls import reverse_lazy #importar o redirecionamento da pagina 
from django.shortcuts import get_object_or_404, redirect
from datetime import date 

from .models import Todo  # vamos na pasta models pegar a classe Todo

class TodoListView (ListView): #pagina todo
    model = Todo 

class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy ("todo_list") # para depois de aplicado voltar a todo list
    

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")

class TodoDeleteView(DeleteView): 
    model = Todo 
    success_url = reverse_lazy("todo_list")


class TodoCompleteView(View):
    def get(self, request, pk): 
        todo = get_object_or_404(Todo, pk=pk)
        todo.finished_at = date.today()
        todo.save()
        return redirect("todo_list")