from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
	list_headere='__all__'

@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
	list_feedBack='__all__'
