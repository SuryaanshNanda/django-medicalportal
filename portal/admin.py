from django.contrib import admin
from .models import Patient,Organisation,Professional,Docsrequest

admin.site.register(Patient),
admin.site.register(Organisation),
admin.site.register(Professional),
admin.site.register(Docsrequest),


# Register your models here.
