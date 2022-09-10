from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManage(BaseUserManager):
    def create_superuser(self, username, password):
        user = self.create_user(  username, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user
    def create_user(self, username, password=None):
        """Crear usuario"""
       
        user = self.model(username=username, password=password)
        user.set_password(password)
        
        user.save(using=self._db)

        return user
    

class UsuarioModel(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(primary_key=True, max_length=45, unique=True)
   
    perfil = models.CharField(max_length=45)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    genero = models.CharField(max_length=45)
    is_staff = models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs) 

    objects= UserManage()
    USERNAME_FIELD = 'username'