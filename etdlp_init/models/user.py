from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class BaseModel(models.Model):
    """
    Columna para borrado lógico
    """
    borrado = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Usuario(AbstractUser, BaseModel):
    class Meta:
        app_label = 'etdlp_init'
