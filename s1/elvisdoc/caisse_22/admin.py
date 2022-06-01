from django.contrib import admin
from .models import etudiants, payements, Enregistrements, caisses, Caissier

# Register your models here.
admin.site.register(etudiants)
admin.site.register(payements)
admin.site.register(Caissier)
admin.site.register(caisses)
admin.site.register(Enregistrements)