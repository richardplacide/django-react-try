from django.db import models

class Formateur(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    contact = models.CharField(max_length=75)

    def __str__(self):
        return self.contact

class Stage(models.Model):
    code_stage = models.CharField(max_length=10)
    intitule = models.CharField(blank=True, max_length=100)
    duree = models.IntegerField(blank=True, null=True)
    formateur = models.ForeignKey('Formateur')
    places = models.IntegerField(blank=True, null=True, default=12)

    def __str__(self):
        return self.code_stage
