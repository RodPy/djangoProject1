from django.contrib import admin

# Register your models here.
from hotel.models import *

admin.site.register(Departamento)
admin.site.register(Dispositivo)
admin.site.register(Piso)
admin.site.register(habitacion)

