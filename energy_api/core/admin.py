from django.contrib import admin

from .models import *

admin.site.register(Societe)
admin.site.register(Compte)
admin.site.register(CompteurElec)
admin.site.register(CompteurGaz)
admin.site.register(DemandeCotation)
admin.site.register(VentePro)
