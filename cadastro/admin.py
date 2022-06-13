from django.contrib import admin
from .models import escola, transportador, rota

# Register your models here.
admin.site.register(escola),
admin.site.register(transportador),
admin.site.register(rota)