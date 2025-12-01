from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from rolepermissions.roles import assign_role

class UserManager(BaseUserManager):
    def _create_user(self, email, perfil, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, perfil=perfil, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, perfil='basic', password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, perfil, password, **extra_fields)

    def create_superuser(self, email, perfil='full', password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(email, perfil, password, **extra_fields)

class Users(AbstractUser):
    email = models.EmailField('E-mail', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    choices_perfil = [
        ('', 'Selecione um perfil'),
        ('full', 'Administrador'),
        ('basic', 'Básico'),
        ('view', 'Visualizador'),
    ]
    perfil = models.CharField(max_length=10, choices=choices_perfil)

    objects = UserManager()

    def __str__(self):  
        return self.email
