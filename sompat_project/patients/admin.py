from django.contrib import admin
from patients.models import Pacient, Aparat

class PacientAdmin(admin.ModelAdmin):
    list_display = ['som_id']

class AparatAdmin(admin.ModelAdmin):
    list_display = ['sn', 'model', 'aktiven']




admin.site.register(Pacient, PacientAdmin)
admin.site.register(Aparat, AparatAdmin)
