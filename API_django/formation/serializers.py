from rest_framework import serializers

from .models import Formateur
from .models import Stage

class FormateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formateur
        fields = ('id', 'nom', 'prenom','contact')

class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = ('id', 'code_stage', 'intitule', 'duree', 'formateur', 'places')
