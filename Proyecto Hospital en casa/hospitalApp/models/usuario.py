from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManage(BaseUserManager):
    def create_user(self, username, contrasenna, perfil, nombre, apellido, telefono, genero):
        """Crear usuario"""
       
        user = self.model(username=username, contrasenna=contrasenna, perfil=perfil, apellido=apellido, nombre=nombre, telefono=telefono, genero=genero )

        
        user.save(using=self._db)

        return user

class UsuarioModel(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(primary_key=True, max_length=45, unique=True)
    contrasenna= models.CharField(max_length=45)
    perfil = models.CharField(max_length=45)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    genero = models.CharField(max_length=45)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.contrasenna = make_password(self.contrasenna, some_salt)
        super().save(**kwargs)

    objects= UserManage()
    USERNAME_FIELD = 'username'