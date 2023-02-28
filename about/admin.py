from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(AboutServices)
class AboutServicesAdmin(admin.ModelAdmin):
	list_about_services='__all__'

@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
	list_headere='__all__'

@admin.register(Achivement)
class AchivementAdmin(admin.ModelAdmin):
	list_achivement='__all__'
