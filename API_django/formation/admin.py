from django.contrib import admin

from .models import Formateur
from .models import Stage

admin.site.register(Formateur)
admin.site.register(Stage)
