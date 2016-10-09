from django.db import models

class Formateur(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    contact = models.CharField(max_length=75)

    def __str__(self):
        return self.contact
        
