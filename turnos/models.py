from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Viernes(models.Model):
    
    horario = models.CharField(null=False)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, null=True, unique=True)
    
    def __str__(self):
        return self.horario
    

class Sabado(models.Model):
    
    horario = models.CharField(null=False)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, null=True, unique=True)
    
    def __str__(self):
        return self.horario