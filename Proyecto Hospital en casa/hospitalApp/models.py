
from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager




"""Modelo de la tabla signos vitales"""
class SignosVitales(models.Model):
    fechaDeMedicion =models.DateTimeField(auto_now=False, auto_now_add=False)
    oximetria = models.DecimalField(decimal_places=2,max_digits=10)
    frecuenciaRespiratoria = models.DecimalField(decimal_places=2,max_digits=10)
    frecuenciaCardiaca = models.DecimalField(decimal_places=2,max_digits=10)
    temperatura = models.DecimalField(decimal_places=2,max_digits=10)
    presionArterial = models.DecimalField(decimal_places=2,max_digits=10)
    glicemias = models.DecimalField(decimal_places=2,max_digits=10)
    
    def __str__(self):
        return str(self.fechaDeMedicion)

"""Modelo De la tabla cargo -Javier Munnoz"""
class Cargo(models.Model):
    nombreCargo=models.CharField(max_length=45)
    def __str__(self):
        self.field_name = self.nombreCargo
        return self.field_name

"""Model de la tabla tipo identificacion -Javier Munnoz"""
class TipoIdentificacion(models.Model):
    tipoidentificacion = models.CharField(max_length=150,null=True)
    def __str__(self):
        self.field_name = self.tipoidentificacion
        return self.field_name

"""Modelo de la tabla PlantaPersonal -Javier Munnoz"""
class PlantaPersonal(models.Model):
    numeroIdentificacion = models.CharField(max_length=45)
    nombrePP= models.CharField(max_length=45)
    apellidoPP= models.CharField(max_length=45)
    direccionPP= models.CharField(max_length=45)
    municipioPP= models.CharField(max_length=45)
    departamentoPP= models.CharField(max_length=45)
    cargo_idCargo= models.ForeignKey(Cargo,on_delete=models.PROTECT)
    tipoIdentificacionPP = models.ForeignKey(TipoIdentificacion,  on_delete=models.PROTECT,null=True)

    def __str__(self):
        self.field_name = self.nombrePP
        return self.field_name


"""Modelo de la tabla pacientes -Javier Munnoz"""
class Pacientes(models.Model):
    tipoIdentificacionPP = models.ForeignKey(TipoIdentificacion, on_delete=models.PROTECT,null=True)
    numeroIdentificacionPaciente = models.IntegerField()
    nombrePaciente = models.CharField(max_length=45)
    apellidosPaciente = models.CharField(max_length=45)
    telefonoPaciente = models.IntegerField()
    direccionPaciente = models.CharField(max_length=45)
    municipio = models.CharField(max_length=45)
    departamento = models.CharField(max_length=45)
    fechaNacimientoPaciente = models.DateField(auto_now=False, auto_now_add=False)
    generoPaciente = models.CharField(max_length=45)
    correo = models.EmailField(max_length=45, unique=True)

    def __str__(self):
        return self.nombrePaciente


"""Modelo tabla historia Clinica -Javier Munnoz"""
class HistoriaClinica(models.Model):
    fehcaHistoriaClinica = models.DateField(auto_now_add=False, auto_now=False)
    paciente = models.ForeignKey(Pacientes,on_delete= models.PROTECT)
    conceptoMedido = models.TextField(max_length=300)
    sugerenciaMedica = models.TextField(max_length=300)
    signosVitales = models.ForeignKey(SignosVitales,on_delete=models.PROTECT,null=True)

    def __str__(self):
        return str(self.fehcaHistoriaClinica)

class Familiar(models.Model):
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    nombreFamiliar = models.CharField(max_length=45)
    apellidoFamilair = models.CharField(max_length=45)
    telefonoFamilair = models.IntegerField()
    direccionFamilair = models.CharField(max_length=45)
    municipio = models.CharField(max_length=45)
    departamento = models.CharField(max_length=45)

"""Creacion de usuarios y modelo en la base de datos de dichos usuarios -Javier Munnoz"""
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
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE, null=True)
    familiar = models.ForeignKey(Familiar,on_delete=models.CASCADE,null=True)
    plantaPersonal = models.ForeignKey(PlantaPersonal, on_delete=models.PROTECT,null=True)

    objects= UserNameManage()
    
    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS= ['name']

    def get_full_name(self):
        """Obtener nombre de usuario"""
        return self.name
    
    def __str__(self):
        """Retornamos el email representando el usuario"""
        return self.correo