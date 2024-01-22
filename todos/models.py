from django.db import models  #classe models


class Todo(models.Model): #estamos puxando da classe models de cima
    title = models.CharField(
        max_length=100, # quanto caracters nesse campo
        null=False, # nao pode ter valores vazios
        blank=False # nao pode espacos vazios 
       
    )
 
    created_at = models.DateTimeField( #data da tarefa foi criada 
        auto_now_add=True, #quando for creada vai puxar a data automatico
        null = False,
        blank= False
        )
    
    deadline = models.DateField(
        null=False,
        blank=False,
    )
    finished_at =models.DateField(
        null=True, # para salvar a data quando for finalziada
    )

    #TODA VEZ QUE MUDAR O MODELS, TEM QUE FAZER O MAKEMIGRATIONS E O MIGRATE