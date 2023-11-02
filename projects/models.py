from django.db import models

# Create your models here.

class Project (models. Model):
    dni = models.CharField(max_length=8, null=True)
    antecedentes_patologicos = models.CharField(max_length=200)
    antecedentes_quirurgicos = models.CharField(max_length=200)
    rams = models.CharField(max_length=200)
    relato_cronologico = models.CharField(max_length=200)
    plan = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)