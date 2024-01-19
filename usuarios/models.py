from django.db import models

# Create your models here.
#vamos criar um modelo personalizado de usuarios 

from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)

class UsuarioManager (BaseUserManager): #interface de como as querys vao ser executada no banco
    def create_user(self, email, password=None):
        usuario = self.model( # modelo de usuario 
            email=self.normalize_email(email)# evita que salve o email com caracteres especiais
) #explicitar o valores
        
        usuario.is_active = True 
        usuario.is_staff= False #estamos criando um usuario comun
        usuario.is_superuser = False

        if password: 
            usuario.set_password(password)
        usuario.save() # salvar o usuario
        return usuario
    
    def create_superuser(self, email, password):
        usuario = self.create_user(
            email=self.normalize_email(email)
        )

        usuario.is_active = True 
        usuario.is_staff= True #estamos criando um super usuario, todos TRUE, acesso! 
        usuario.is_superuser = True
        
        usuario.set_password(password)
        usuario.save()
        return usuario
        

class Usuario(AbstractBaseUser, PermissionsMixin): #funcao usuario
    
    email = models.EmailField ( #existrem vários tipos de campos
        verbose_name = "Email do usuario", # nome para o field
        max_length=200, # tamanho do email 
        unique=True, #nao pode existe dois usarios com dois emails 
    )

    is_active = models.BooleanField(
        verbose_name = "usuario está ativo",
        default=True,
    )

    is_staff = models.BooleanField(
        verbose_name="usuario é da equipe de desenvolvimento",
        default=False, #pode existe mais de dois usuarios
    )

    is_superuser = models.BooleanField(
        verbose_name= "Usuiario é um superusuario",
        default=False,
    )

    USERNAME_FIELD = "email"

    objects = UsuarioManager() #para criar os usuarios e super usuarios

    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"
        db_table = "usuario"

    def __str__(self): #estancia, para fins de exibicao 
        return self.email