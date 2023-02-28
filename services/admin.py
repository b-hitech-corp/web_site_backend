from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
	list_services='__all__'