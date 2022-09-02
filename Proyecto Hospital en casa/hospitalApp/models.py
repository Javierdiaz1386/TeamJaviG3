import email
from errno import EMSGSIZE
from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserNameManage(BaseUserManager):
    def create_user(self, correo, name, password=None):
        """Crear usuario"""
        if not correo:
            raise ValueError('Usuario debe tener un email')

        correo = self.normalize_email(correo)
        user = self.model(correo=correo, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, correo, name, password):
        user = self.create_user(correo, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """Modelo base de datos para usuarios en el sistema"""
    correo= models.EmailField(max_length=255,unique=True)
    name= models.CharField(max_length=255)
    is_active= models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False)

    objects= UserNameManage()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS= ['name']

    def get_full_name(self):
        """Obtener nombre de usuario"""
        return self.name
    
    def __str__(self):
        """Retornamos el email representando el usuario"""
        return self.correo

    


    